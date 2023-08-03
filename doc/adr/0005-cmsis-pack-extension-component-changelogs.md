# 5. Extend Open-CMSIS-Pack for per component changeLogs

Date: 2021-05-11

## Status

Accepted

## Context

Open-CMSIS-Pack specification supports recording changeLogs as part of the releases section. Hence one cannot easily
deduce which changes apply to which component(s).

## Decision

Follow the approach already used for `<conditions>` in the current [Pack Description](../Glossary.md#pack-desc)
using references:
* add optional section `<changeLogs>` on the top level of the format
* add one or more child elements `<changelog>` to `<changeLogs>` with attributes:
    * `id` (required) - a unique name which is used by components to associate itself with a `changelog`
    * `name` (required) - the relative path to the changelog file
    * `type` (optional) - mime-type of the changelog file, defaults to `text/plain;charset=UTF-8`
    * `default` (optional) - the default changelog is automatically associated with all components/apis, default to false
* add optional attribute `changelog` to `<component>` element.
* add optional attribute `changelog` to `<api>` element.
* add optional attribute `changelog` to `<bundle>` element.

## Consequences

* Complexity of package description increases
* the default mechanism allows to specify a single `changelog` for all components of a pack conveniently.
* Validation tool is required to test:
    * for each `<changelog>` that name is specified, unique (within pdsc) and file exists
	* a maximum of one `changelog` has attribute `default="true"` set
    * for each `<component>` that attribute `changelog` unique ID exists (within pdsc)
    * for each `<api>` that attribute `changelog` unique ID exists (within pdsc)
    * for each `<bundle>` that attribute `changelog` unique ID exists (within pdsc)
* Pack Manager requires extension
    * display changelog information per component
