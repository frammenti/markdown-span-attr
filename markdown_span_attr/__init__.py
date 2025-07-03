"""
Span Attribute Extension for Python-Markdown

Wraps inline content in <span> elements using attribute list syntax:

    [content]{: #id .class key="value" }

GitHub: https://github.com/frammenti/markdown-span-attr
PyPI: https://pypi.org/project/markdown-span-attr/

Copyright 2025 Francesca Massarenti
License: MIT
"""

from .span_attr import SpanExtension

def makeExtension(**kwargs):
    return SpanExtension(**kwargs)