# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Graz University of Technology.
#
# invenio-alma is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Invenio module to connect InvenioRDM to Alma."""

from .ext import InvenioAlma
from .version import __version__

__all__ = ("__version__", "InvenioAlma")
