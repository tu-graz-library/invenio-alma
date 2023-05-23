# -*- coding: utf-8 -*-
#
# Copyright (C) 2021-2023 Graz University of Technology.
#
# invenio-alma is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Utils."""

from __future__ import annotations

import functools
from collections.abc import Callable

from flask import current_app
from invenio_config_tugraz import get_identity_from_user_by_email
from invenio_records_marc21 import current_records_marc21

from .services import AlmaRESTService, AlmaSRUService
from .services.config import AlmaRESTConfig, AlmaSRUConfig
from .services.errors import AlmaAPIError


def is_duplicate_in_alma(cms_id: str) -> None:
    """Check if there is already a record in alma."""
    search_key = "local_field_995"
    domain = current_app.config["ALMA_SRU_DOMAIN"]
    institution_code = current_app.config["ALMA_SRU_INSTITUTION_CODE"]
    config = AlmaSRUConfig(search_key, domain, institution_code)
    sru_service = AlmaSRUService.build(config)

    try:
        record = sru_service.get_record(cms_id)
        return len(record) > 0
    except AlmaAPIError:
        return False


def preliminaries(
    user_email: str,
    config: AlmaRESTConfig | AlmaSRUConfig = None,
    *,
    use_rest: bool = False,
    use_sru: bool = False,
) -> tuple:
    """Preliminaries to interact with the repository."""
    records_service = current_records_marc21.records_service

    if use_rest:
        alma_service = AlmaRESTService.build(config)
    elif use_sru:
        alma_service = AlmaSRUService.build(config)
    else:
        msg = "choose between using rest or sru."
        raise RuntimeError(msg)

    identity = get_identity_from_user_by_email(email=user_email)

    return records_service, alma_service, identity


def apply_aggregators(aggregators: list[Callable[[], list]]) -> list:
    """Apply aggregators."""

    def func(accumulator: list, aggregator: Callable) -> list:
        return accumulator + aggregator()

    return functools.reduce(func, aggregators, [])
