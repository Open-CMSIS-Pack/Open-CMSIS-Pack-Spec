# Schema Change

This pull request contributes a change to an Open-CMSIS-Pack file schema.
Schema changes have a major impact on the tool ecosystem and need to be done carefully.

## Description

:warning: Explain the reason for the proposed schema change. Add a references to the ADR implemented. Add a reference to the associated PR to [PackChk](https://github.com/Open-CMSIS-Pack/devtools/tree/main/tools/packchk).

## Checklist

_checklist version 2021-11-10_

- [ ] Does this change implement an approved ADR?
      If yes is the reference provided in the description above?
- [ ] Is the schema file changed, properly?
  - [ ] Is the schema version incremented according to [Semantic Versioning](https://semver.org/)?
  - [ ] Is the schema file header updated, version and date?
  - [ ] Is the schema file change history updated?
  - [ ] Does the updated schema file pass [XSD meta schema](https://www.w3.org/2012/04/XMLSchema.xsd) check?
- [ ] Is the documentation updated, accordingly?
- [ ] Are the [automatic checks](../tree/main/.github/workflows) updated or enhanced if required?
- [ ] Are enhancements to [PackChk](https://github.com/Open-CMSIS-Pack/devtools/tree/main/tools/packchk) required to proof semantic usage of changed/added features?
      If yes is the reference to the pull request provided in the description above?
