# -*- coding: utf-8 -*-
#
# Copyright (C) 2021-2024 Graz University of Technology.
#
# invenio-alma is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Celery Tasks for invenio-alma."""

from celery import shared_task
from flask import current_app
from invenio_access.permissions import system_identity

from .proxies import current_alma
from .services import AlmaRESTError
from .utils import apply_aggregators


@shared_task(ignore_result=True)
def create_alma_records() -> None:
    """Create records within alma from repository records."""
    aggregators = current_app.config["ALMA_ALMA_RECORDS_CREATE_AGGREGATORS"]
    create_func = current_app.config["ALMA_ALMA_RECORDS_CREATE_FUNC"]

    if not aggregators:
        msg = "ERROR: variable ALMA_REPOSITORY_RECORDS_CREATE_AGGREGATORS not set."
        current_app.logger.error(msg)
        return

    if not create_func:
        msg = "ERROR: variable ALMA_ALMA_RECORDS_CREATE_FUNC not set"
        current_app.logger.error(msg)
        return

    alma_service = current_alma.alma_rest_service
    ids = apply_aggregators(aggregators)

    for marc_id, cms_id in ids:
        try:
            create_func(system_identity, marc_id, cms_id, alma_service)
        except (RuntimeError, RuntimeWarning) as error:
            msg = "ERROR: creating record in alma. (marcid: %s, cms_id: %s, error: %s)"
            current_app.logger.error(msg, marc_id, cms_id, error)


@shared_task(ignore_result=True)
def update_repository_records() -> None:
    """Update records within the repository from alma records."""
    aggregators = current_app.config["ALMA_REPOSITORY_RECORDS_UPDATE_AGGREGATORS"]
    update_func = current_app.config["ALMA_REPOSITORY_RECORDS_UPDATE_FUNC"]

    if not aggregators:
        msg = "ERROR: variable ALMA_REPOSITORY_RECORDS_UPDATE_AGGREGATORS not set."
        current_app.logger.error(msg)
        return

    if not update_func:
        msg = "ERROR: variable ALMA_REPOSITORY_RECORDS_UPDATE_FUNC not set."
        current_app.logger.error(msg)
        return

    alma_service = current_alma.alma_sru_service
    ids = apply_aggregators(aggregators)

    for marc_id, alma_id in ids:
        try:
            update_func(system_identity, marc_id, alma_id, alma_service)
        except Exception as error:  # noqa: BLE001
            msg = "ERROR: updating records within the repository."
            msg += " (marc21_id: {marc_id}, alma_id: {alma_id}, error: {error})"
            current_app.logger.error(msg, marc_id, alma_id, error)
