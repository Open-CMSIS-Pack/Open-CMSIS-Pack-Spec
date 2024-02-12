# Open-CMSIS-Pack Specification

The Open-CMSIS-Pack project delivers the infrastructure to integrate and manage software components and improve code reuse across embedded and IoT projects. The project is currently hosted and managed as an incubation project by Linaro in partnership with Arm, NXP and ST.

This Open-CMSIS-Pack specification is part of the Common Microcontroller Software Interface Standard and covers the following areas:

- **Pack:** Describes a delivery mechanism for software components, device parameters, and evaluation board support. It simplifies software re-use and product life-cycle management (PLM).
 
- **Build:** Defines the build tools for project based on software packs.


Linaro Project: [Open-CMSIS-Pack](https://linaro.atlassian.net/wiki/spaces/CMSIS/overview)

## Access to Specification 

The specification is pre-build and can be accessed here: [https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/index.html](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/index.html)

## License

The Open-CMSIS-Pack project and its sub-components are licensed under Apache 2.0.

## Contributions and Pull Requests

Contributions are accepted under Apache 2.0. Only submit contributions where you have authored all of the code.

### Proposals, Reviews and Project
Please feel free to raise an [issue on GitHub](https://github.com/Open-CMSIS-Pack/Open-CMSIS-Pack/issues)
to start the discussion about your proposal.

We discuss proposals which we are dividing into 5 work streams with a dedicated label:

- **Core Library Components** - common libraries that are re-used across a range of tools. The PoC Tools are the first consumers, but the library components can also be used to create commercial derivatives or inhouse tooling.
- **Overall Project Concept** - procedures to generate packs and application software. We will consider complex applications such as multi-core processor systems or secure/non-secure partitions.
- **PoC Tools** - command line tools and utilities that implement the overall concepts and are indented to be used for open-source projects or even integrated into commercial software tools.
- **Process Improvements** - documentation and tools that help the software community to streamline and secure the software delivery to the user base.
- **Resource Management** - describes the data models used to manage and organized software packs and application projects.

These Issues are tracked inside the [project board](https://github.com/Open-CMSIS-Pack/Open-CMSIS-Pack/projects/1)

### Issues, Labels
Please feel free to raise an [issue on GitHub](https://github.com/Open-CMSIS-Pack/Open-CMSIS-Pack/issues)
to report misbehavior (i.e. bugs)

Issues is your best way to interact directly with the maintenance team and the community.
We encourage you to append implementation suggestions as this helps to decrease the
workload of the very limited maintenance team. 

We will be monitoring and responding to issues as best we can.
Please attempt to avoid filing duplicates of open or closed items when possible.
In the spirit of openness we will be tagging issues with the following:

- **bug** – We consider this issue to be a bug that will be investigated.

- **wontfix** - We appreciate this issue but decided not to change the current behavior.
	
- **out-of-scope** - We consider this issue loosely related to CMSIS. It might by implemented outside of CMSIS. Let us know about your work.
	
- **question** – We have further questions to this issue. Please review and provide feedback.

- **documentation** - This issue is a documentation flaw that will be improved in future.

- **DONE** - We consider this issue as resolved - please review and close it. In case of no further activity this issues will be closed after a week.

- **duplicate** - This issue is already addressed elsewhere, see comment with provided references.

### Pull Requests
When raising a Pull Request (PR) changing the PACK.xsd schema file, please ensure that the version, date of change, release-notes and 
documentation get updated consistently throughout your PR. 

Rules: 
- Breaking/incompatible changes are not accepted and require further discussion

Exceptions: 
- Extending the `DeviceVendorEnum` does not require a version increment of the schema version.

Step 1:
Edit the PACK.xsd file updating `<date>=dd. mmm yyyy` and `<version>=major.minor.patch` (Semantic Version) in:
- `$Date: <date>`
- `$Revision: <version>`
- `SchemaVersion=<version>`
- Release Notes: `<date>: v<version>` and add itemized changes
- `<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" ... version="<version>">`

Step 2:
Edit the doxygen documentation located in "doxygen/src/*.txt"
- add/update the documentation to reflect the proposed change following the existing document structure.
- update the Release Notes section in "doxygen/src/General.txt" matching the itemized list in PACK.xsd.
- update the version of the documentation `PROJECT_NUMBER= "Version <version>"` in "doxygen/pack.dxy" to match the schema version.

