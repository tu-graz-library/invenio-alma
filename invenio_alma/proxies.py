# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
#
# Copyright (C) 2022-2025 Graz University of Technology.
#
# Invenio-Alma is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Helper proxy to the state object."""

from typing import cast

from flask import current_app
from werkzeug.local import LocalProxy

from .ext import InvenioAlma

current_alma: InvenioAlma = cast(
    InvenioAlma,
    LocalProxy(lambda: current_app.extensions["invenio-alma"]),
)
"""Helper proxy to get the current alma extension."""
