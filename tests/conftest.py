# -*- coding: utf-8 -*-
#
# Copyright (C) 2021-2025 Graz University of Technology.
#
# invenio-alma is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Pytest configuration.

See https://pytest-invenio.readthedocs.io/ for documentation on which test
fixtures are available.
"""

from collections.abc import Callable

import pytest
from flask import Flask

from invenio_alma import InvenioAlma


@pytest.fixture(scope="module")
def create_app(instance_path: str) -> Callable:
    """Application factory fixture."""

    def factory(**config: dict) -> InvenioAlma:
        app = Flask("testapp", instance_path=instance_path)
        app.config.update(**config)
        app.config["ALMA_API_KEY"] = "test-token"
        app.config["ALMA_API_HOST"] = "test-host"
        InvenioAlma(app)
        return app

    return factory
