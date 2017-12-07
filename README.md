# cms_figure

The CMS Publication Committee has a set of [guidelines](https://twiki.cern.ch/twiki/bin/view/CMS/Internal/FigGuidelines) regarding how figures should appear in more official settings. To that end, they provide a ROOT C++ macro for drawing figure labels that is accompanied by an all too literal translation into Python. Both versions suffer from vague parameter names, unintuitive values for arguments, and lack of documentation.

Having worked on restyling figures for publication, I decided to craft a more user-friendly experience for myself and others. The end result is this unofficial `cms_figure` package that features:

* The `TDRStyle` context manager that helps with switching to and from the official plotting style.
* The `draw_labels` utility function that positions and draws figure labels on the active canvas.
* The `CMSLabel` and `LuminosityLabel` classes for power users that need customization beyond typical use-cases covered by `draw_labels`.
* And docstrings. Docstrings everywhere!
