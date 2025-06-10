# -*- coding: utf-8 -*-
#
# Copyright (C) 2025 Graz University of Technology.
#
# invenio-alma is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Jobs."""

from invenio_jobs.jobs import JobType, PredefinedArgsSchema
from invenio_jobs.models import Job
from marshmallow.fields import String

from .tasks import create_alma_records, update_repository_records


class AlmaPredefinedArgsSchema(PredefinedArgsSchema):
    """Alma predefined args schema."""

    workflow = String(
        metadata={
            "description": "choose workflow to run the task",
        },
    )


class CreateAlmaRecordsJob(JobType):
    """Create alma records job."""

    id = "create_alma_records"
    title = "Create Record in Alma"
    description = "Create recods in alma"

    task = create_alma_records

    arguments_schema = AlmaPredefinedArgsSchema

    @classmethod
    def build_task_arguments(
        cls,
        job_obj: Job,  # noqa: ARG003
        workflow: str | None = None,
        **__: dict,
    ) -> dict[str, str]:
        """Define extra arguments to be injected on task execution."""
        return {"workflow": workflow}


class UpdateRepositoryRecordsJob(JobType):
    """Update repository records job."""

    id = "update_repository_records"
    title = "Update repository-record from Alma"
    description = "Update record in the repository."

    task = update_repository_records

    arguments_schema = AlmaPredefinedArgsSchema

    @classmethod
    def build_task_arguments(
        cls,
        job_obj: Job,  # noqa: ARG003
        workflow: str | None = None,
        **__: dict,
    ) -> dict[str, str]:
        """Define extra arguments to be injected on task execution."""
        return {"workflow": workflow}
