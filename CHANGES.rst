..
    Copyright (C) 2021 Graz University of Technology.

    invenio-alma is free software; you can redistribute it and/or modify it
    under the terms of the MIT License; see LICENSE file for more details.

Changes
=======

Version v0.5.0 (release 2022-10-02)

- change: add timeout to requests.(get|put)
- fix: invenio_search.engine hides used search tool
- global: add supported python versions
- global: move to reusable workflows
- global: migrate from elasticsearch to opensearch
- fix AlmaAPIError missing paramete use
- harmonize the alma service error messages
- use for duplicate error message same structure as for the others


Version v0.4.4 (release 2022-08-03)

- improve duplicate output by adding the repository id
- fix RequestError problem, by handling the error


Version v0.4.3 (release 2022-08-02)

- add ac number to the success output
- fix ValidationError problem


Version v0.4.2 (release 2022-08-02)

- remove no_self_use, pylint Closes #5502
- fix elasticsearch ConnectionTimeout import
- fix sphinx language


Version v0.4.1 (release 2022-08-02)

- fix elasticsearch ConnectionTimeout problem


Version 0.1.0 (released TBD)

- Initial public release.
