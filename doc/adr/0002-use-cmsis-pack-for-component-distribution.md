# ADR 2: Use CMSIS-Pack for component distribution

Date: 2020-12-08

## Status

Accepted

## Context

We need to be able to pack and distribute software components under their
sources and pre-compiled binary. The technology selected must also manage
dependencies between components and ideally offer some support for configuring an
individual component.

The component descriptor must be human readable (text-based) but may benefit
from tools to generate/update it.

How popular a solution is, in terms of available package and community
engagement is also a critical aspect as it directly impacts the efforts we will
need to put in to achieve a viable adoption level.

The solution chosen must be developed in an open source and open governance
model.

We do not mandate a pack registry. If one comes with the pack architecture it
must allow for additional registry to fetch from.

It is intentionally left to the downstream _distribution_ maintainers
(Zephyr/Mbed) to manage compatibility of the components.

We evaluated some of the major solution currently available on the market:

- [Conan.io](conan.io)

  Using it for cortex-m class target is a stretch<sup id="a1">[1](#fn1)</sup>
  of the tool. The integration with the build system(s) requires changes in
  to the tool itself<sup id="a2">[2](#fn2)</sup> (which is not desired) provided that
  we do not have control over the technology.

- [CMSIS-Pack](https://arm-software.github.io/CMSIS_5/Pack/html/index.html)

  Mostly used within Keil uVision, this solution is already used by silicon partners
  to distribute some parts of their SDK. Although it is based on XML and
  requires tools to efficiently maintain it, it does provide all the necessary
  features. The CMSIS-Pack index counts 640 unique packages. Excluding device
  specific packages<sup id="a4">[4](#fn4)</sup> leaves around 70 packages,
  around 10 of which are `nRF_`packages and 37 are published either on
  http://www.keil.com/pack/ or https://github.com/MDK-Packs/Pack.

- [Yotta](https://yottabuild.org/)

  Yotta is a serious contender to CMSIS-Pack in terms of offered featured and
  available components. The dependency architecture and strategy is already
  well defined. Based on JSON it is easy to create, and maintain. CLI tools
  already exist, rendering the user experience rather fluid. A previous attempt
  at using Yotta in Mbed OS faced strong rejection mostly due to regular
  breakage in the ecosystem. It seems that those issues were not much due to
  problem in the tool itself but rather to bad practice around the
  [semver](semver.org) rules. Yotta is not actively maintained. Yotta counts
  __314__ unique packages (excluding the test packages `test1`, `test2`, …).
  Excluding the device specific packages leaves around 200 middleware and
  external peripheral drivers<sup id="a3">[3](#fn3)</sup>.

- [lbuild](https://github.com/modm-io/lbuild)

  Even though it presents some really interesting features around code
  generation and code configuration it does not have enough effective adoption
  to become a serious contender since it would mean starting the adoption
  process from scratch.

_Note:_ The number of packages is highly influenced by how the packages are
bundled (by family/subfamily or package hierarchy). Thus the number of devices
supported is hard to evaluate and compare but can generally be considered
_large enough_ (yotta benefiting from mbed's large portability).

## Decision

Considering the relative maturity, adoption, and the ability to contribute to
these projects under an open source and open governance model, we've decided to
use CMSIS-Pack as the starting point for Component specification.

The process of evolving CMSIS-Pack is strictly guided by approved User Stories​.
Breaking backward compatibility is acceptable given a viable migration story is
provided.

## Consequences

As raised by partners during a previous meeting,
there's room for improvement on CMSIS-Packs but nothing that cannot be
addressed on upcoming iterations. The group acknowledges the risk that evolving
CMSIS-Pack might be slower to address requirements that substantially deviate
from today's concepts than starting from scratch​.

Partners and Arm parties specifically raised the following topics:
- A system integrator may need a fix in a component and cannot wait for it to
  be upstreamed before shipping. A _pack customisation_ model must be defined.
- Authentication of component will become a serious concern as the ecosystem
  develops. We will need to define a strategy to address that.

Tools will need to be developed to ease the use of this technology. These
will most probably need to evolve along with the specification in order to
address feedback from the partners.

Ideally the technology (specification and tools) should go under an
open-governance in order to ease contribution and accelerate its adoption.

## Footnotes

<b id="fn1">1</b>: https://github.com/conan-io/conan/issues/86#issuecomment-359483915 [↩︎](#a1)
<b id="fn2">2</b>: https://github.com/conan-io/conan/pull/1494 [↩︎](#a2)
<b id="fn3">3</b>: Extracted from mongodb's documents with `db.modules.find({}, {"json.name": 1, _id: 0}).map((entry) => { return entry.json.name }).sort().filter((el,i,a) => {return i===a.indexOf(el) && !el.startsWith("test")})`
and extra manual filtering to remove device specific packages. [↩︎](#a3)
<b id="fn4">4</b>: Extracted from https://sadevicepacksprodus.blob.core.windows.net/idxfile/index.pidx.
Excluding device specific packages by filtering out name ending with **BSP** and **DFP** plus some
extra filtering to remove device from vendors such as HDSC or maxim that are not ending with those
tags. [↩︎](#a4)
