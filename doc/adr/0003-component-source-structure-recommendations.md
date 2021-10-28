# ADR 3: Component source structure recommendations

Date: 2020-08-07

## Status

Proposed

## Context

Open-CMSIS-Pack encourages componentization of software with meaningful APIs. The
componentization enables parallel development, maintenance and distribution of
software components. These components can come from multiple vendors,
therefore it is very useful to unify the structure of component source trees.
In addition, unified source structure helps with,

* Better maintenance of components
* Easy navigation through source

## Decision

The following directory structure is recommended for new Open-CMSIS-Pack components:

```console
<component_name>
├── CONTRIBUTING.md
├── LICENSE.md
├── README.md
├── docs
├── examples
│   └── <example_name>
│       └── <example_name>.cpp
├── include
│   └── <component_name>
│       └── <component_name>.h
├── src
│   └── <component_name>.cpp
├── templates
│   └── <component_name>_template.cpp
└── tests
    └── <component_name>_test.cpp
```

### Top level directory

Named after the component. It is recommended to use `_` (underscore)
as word separator instead of space(e.g., `mbed_events`).

### Contribution

Contribution guidelines may be added to `CONTRIBUTING.md`. It may also
specify the *license* under which contribution will be accepted.

### License

Every component should contain license details. We recommend the following:

* Single license

    The license text should be added to `LICENSE.md`. For example, to release a
    component under Apache 2.0, the full original
    [Apache 2.0 license text](http://www.apache.org/licenses/LICENSE-2.0) should
    be in `LICENSE.md`.

* Multiple licenses

    A `LICENSE.md` file with the following text:
    ```
    Unless specifically indicated otherwise in a file, files are licensed under
    the Apache 2.0 license, as can be found in: LICENSE-apache-2.0.txt
    ```
    The full original
    [Apache 2.0 license text](http://www.apache.org/licenses/LICENSE-2.0) in
    LICENSE-apache-2.0.txt.

    Each source header should start with copyright line, the SPDX identifier
    and the license header:
    ```
    Copyright (c) [First year]-[Last year], **Your Name or Company Here**
    SPDX-License-Identifier: <License-name>
    <License-header>
    ```

    In order to release the component under different license, update `LICENSE.md`
    with desired license details and add full license text to
    `LICENSE-<license-name>.txt`

* Component with only binary

    A `LICENSE.md` file with the following text:
    ```
    Unless specifically indicated otherwise in a file, files are licensed under the Permissive Binary License, as can be found in LICENSE-permissive-binary-license-1.0.txt
    ```
    The full original
    [Permissive Binary License 1.0 text](https://os.mbed.com/licenses/permissive-binary-license/)
    in LICENSE-permissive-binary-license-1.0.txt.

### Documentation

The `README.md` may contain brief introduction to the component and detailed
documentation may be added under `docs` directory. Also, for components hosted
on GitHub, this allows easily sharing the docs via GitHub pages, as GitHub
pages can share either the root of a repo or its `docs` directory.

### Examples

The `examples` directory may contain examples which demonstrate the use of the
component. Each directory under `examples` should only contain one example. It is
strongly recommended that examples are kept up-to-date and maintained such
that they can be compiled and tested.

```console
├── examples
│   └── example1
│   └── example2
```

### Headers

All header files, including API header, should be added to `include/<component_name>`
(e.g., `include/mbed_events/mbed_events.h`). This convention
forces API consumers to add component name while including API headers which
avoids header inclusion collisions (e.g., `#include "mbed_events/mbed_events.h"`).

### Sources

All source files should be added to the `src` directory.

### Templates

Templates are application outlines which can act as a starting point for
application developers. The only difference between `examples` and
`templates` is that `examples` are complete and work out-of-the-box,
whereas `templates` may not. If a component is providing a template then it
should be added to the `templates` directory.

### Tests

It's strongly recommended that every component contains at least unit test
cases added in the `tests` directory.

## Consequences

The component directory structure is recommended rather than enforced/mandated.
Therefore it might be possible that existing components might not be migrated
to the recommended directory structure. Due to the same reason, new components might
not use the recommended directory structure.
