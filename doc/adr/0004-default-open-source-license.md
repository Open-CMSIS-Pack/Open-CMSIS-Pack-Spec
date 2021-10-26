# ADR 4: Default Licenses for Open-CMSIS-Pack content

Date: 2020-11-24

## Status

Accepted

## Context

Open-CMSIS-Pack content (such as specs, code, etc) needs to be licensed properly so
that it can be widely adopted. The default license shall be permissive to
allow adoption for proprietary and commercial use, free from copy-left
obligations.

A couple of well known Open Source Licenses have been taken into account:

- [BSD 3-Clause License](https://opensource.org/licenses/BSD-3-Clause)
- [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)
- [MIT License](https://opensource.org/licenses/MIT)
- [Creative Commons CC-BY-SA 4.0][https://creativecommons.org/licenses/by-sa/4.0/legalcode]

## Decision

By default all publicly published Open-CMSIS-Pack software is to be licensed under
the Apache v2.0 license. However, Open-CMSIS-Pack may reuse software already licensed
under another license, provided the license is permissive in nature and
compatible with Apache v2.0. Documentation shipped alongside the code shall be
licensed under the same license as the code.

Specifications are to be licensed under the Creative Commons CC-BY-SA 4.0
license (Creative Commons  Attribution-ShareAlike 4.0 International Public
License).

All contributions to software and documents are licensed by contributors under
the same license model as the software/document itself (ie. inbound == outbound
licensing).

## Consequences

The Apache License 2.0 grants permissive use to everybody, including
adoption for proprietary and commercial use. It does not contain any
copy-left obligations.

The Creative Commons CC-BY-SA 4.0 permissive use to everybody, including
adoption for proprietary and commercial use. It does not contain any
copy-left obligations.
