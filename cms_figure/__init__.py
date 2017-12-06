# -*- coding: utf-8 -*-
"""
cms_figure
==========

This module provides classes and functions for styling plots made
using ROOT according to the CMS Publication Committee standards.

:copyright: (c) 2017 by Sean-Jiun Wang.
:license: MIT, see LICENSE for more details.
"""

__version__ = '0.1.0'

# Core classes
from .labels import CMSLabel, LuminosityLabel

from .tdr_style import TDRStyle

# Utilities
from .utils import draw_labels

__all__ = [
    # Core classes
    'CMSLabel', 'LuminosityLabel', 'TDRStyle',

    # Utilities
    'draw_labels',
]

