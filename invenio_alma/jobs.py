# -*- coding: utf-8 -*-
#
# Copyright (C) 2025 Graz University of Technology.
#
# invenio-alma is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Jobs."""

from invenio_jobs.jobs import JobType

from .tasks import create_alma_records, update_repository_records


class CreateAlmaRecordsJob(JobType):
    """Create alma records job."""

    id = "create_alma_records"
    title = "Create Alma Records"
    description = "Create alma records"

    task = create_alma_records


class UpdateRepositoryRecordsJob(JobType):
    """Update repository records job."""

    id = "update_repository_records"
    title = "Update Repository Records"
    description = "Update repository records"

    task = update_repository_records
