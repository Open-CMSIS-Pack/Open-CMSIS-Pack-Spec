# Proposal: improved CMSIS debug sequence handling

All values are unsigned 64-bit integers.

## Sequence parameters and arguments

- Declare `<parameter>` children at the top of `<sequence>`, before any `<block>`,
  `<control>`, or `<return>`. Both `name` and `default` are mandatory. Names must
  be unique; defaults must be constants.
- Call arguments use `name = value`, where the value can be an expression.
  Supply arguments for declared parameters in any order, each name at most once.
  Unknown or repeated names are errors. Omitted arguments use the corresponding
  `<parameter>` default.
- Argument expressions are evaluated left to right in the caller and passed by
  value. Parameters are local variables in the called sequence and its child
  controls; assignments affect only that invocation's copy. Existing variable
  naming and no-redefinition rules apply.

```xml
<sequence name="AddValues">
  <parameter name="left" default="0"/>
  <parameter name="right" default="0"/>
  <return value="left + right"/>
</sequence>

<sequence name="ArgumentExample">
  <block>
    __var base = 10;
    __var sum = Sequence("AddValues", right = base + 4, left = 2);
    __var withDefault = Sequence("AddValues", left = 3);
    // sum is 16; withDefault is 3.
  </block>
</sequence>
```

## Sequence return values

- `<return>` has an optional `value` attribute containing an unsigned 64-bit
  number or an expression resolving to one. If omitted, `value` defaults to `0`.
- When reached, `<return>` evaluates its value and ends the current sequence,
  including any enclosing controls. The calling `Sequence()` returns that value,
  and the caller continues execution.
- Reaching the end without executing `<return>` yields `0`. Existing abort
  behavior and save/restore rules for `__dp`, `__ap`, `__apid`, and
  `__errorcontrol` apply.

```xml
<sequence name="SelectValue">
  <parameter name="enabled" default="0"/>
  <parameter name="value" default="1"/>
  <control if="enabled">
    <return value="value"/>
  </control>
</sequence>
```

## Last function error

`__lasterror` is a predefined, read-only variable that can always be read.

- It clears to `0` when a debug access function begins execution, after argument
  evaluation. Errors set it to `-1` unless detailed codes are specified for a
  function.
- Inspect or copy it before another function call clears it. Variable reads and
  arithmetic without function calls do not clear it.
- In an atomic block, it updates after block execution. Do not use it as input
  to another debug access function within that block.
- `__errorcontrol` bit 0 must be `1` to continue after an error. Otherwise,
  execution aborts before the sequence can read `__lasterror` again.

Debugger error output should identify the failing function and sequence
location. Split complex expressions and nested calls into separate statements
when this makes execution easier to follow.

```xml
<sequence name="ProbeRead">
  <parameter name="address" default="0"/>
  <block>
    __var savedErrorControl = __errorcontrol;
    __errorcontrol = __errorcontrol | 1;
    Read32(address);
    __var accessError = __lasterror;
    __errorcontrol = savedErrorControl;
  </block>
  <return value="accessError"/>
</sequence>
```

## Errors, results, and return values

| Mechanism | Purpose |
| --- | --- |
| `__lasterror` | Engine-reported error status of the last debug access function call. |
| `__Result` | Status reported to the debugger: `0` for success, `-1` for error. |
| Sequence return value | Numeric value returned to the caller of `Sequence()`. Its interpretation is defined by the sequence implementation. |

- The debugger initializes `__Result` to `0` before invoking a sequence and uses
  it as the status when execution returns to the debugger. Nested `Sequence()`
  calls do not reinitialize or stack it; assignments remain visible to the caller.
- A sequence's return-value format may have no space for an error indicator.
  It can encode errors only if the format defined by its implementation allows
  it. `__Result` reports status independently of the returned value.
- For `Sequence()`, `__lasterror` is nonzero only if the call itself fails, for
  example due to invalid call arguments. It does not propagate errors from
  functions inside the called sequence. If needed, the called sequence can set
  `__Result` to `-1` when its `__lasterror` is nonzero.
- Returning a value does not implicitly modify `__lasterror` or `__Result`.
  Assigning `__Result` does not end sequence execution or supply a return value.

## Global declarations

| Element | Sequence access | Initialization |
| --- | --- | --- |
| `<debugvars>` | Read-write | Device settings > `.dbgconf` > declared value |
| `<debugconsts>` | Read-only | Declared value; no configuration overrides |
| `<debugglobals>` | Read-write | Declared value; no configuration overrides |

- All three elements use `__var` declarations with mandatory constant unsigned
  64-bit initializers. Expressions are not allowed.
- Existing `<debugvars>` declarations become read-write. Only `<debugvars>`
  variables can be configured through [`device-settings:`](https://open-cmsis-pack.github.io/cmsis-toolbox/pyOCD-Debugger/#device-settings) nodes in `csolution.yml`
  and `.dbgconf` files, with device settings taking precedence.
- The engine is generally initialized before the first sequence execution of a
  session; its state is discarded after the last. Exact timing and session
  boundaries depend on the debugger's strategy and use case.
- After initialization, all three groups are global within the engine and shared
  by all its sequences. Sequence calls do not stack these variables. Writable
  values persist across calls. Leaving a sequence or control does not destroy
  them; entering a sequence does not reapply initializers or configuration
  overrides.
- Sequences must explicitly assign variables from `<debugvars>` or
  `<debugglobals>` when reinitialization is needed.
- Updates to `<debugvars>` and `<debugglobals>` variables are not guaranteed to
  be atomic. Debug sequences are not expected to execute concurrently.

```xml
<debugvars>
  __var BoardOption = 0;
</debugvars>

<debugconsts>
  __var MaxBufferSize = 4096;
</debugconsts>

<debugglobals>
  __var CachedState = 0;
</debugglobals>

<sequence name="ClearCachedState">
  <block>
    CachedState = 0;
  </block>
</sequence>
```
