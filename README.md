# cms_figure

The CMS Publication Committee has a set of [guidelines](https://twiki.cern.ch/twiki/bin/view/CMS/Internal/FigGuidelines) regarding how figures should appear in more official settings. To that end, they provide a ROOT C++ macro for drawing figure labels that is accompanied by an all too literal translation into Python. Both versions suffer from vague parameter names, unintuitive values for arguments, and minimal documentation.

Having worked on restyling figures for publication, I decided to craft a more user-friendly experience for myself and others. The end result is this unofficial cms_figure package that features:

* A `TDRStyle` context manager that helps with switching to and from the official plotting style.
* A `draw_labels` utility function that positions and draws figure labels on the active canvas.
* The `CMSLabel` and `LuminosityLabel` classes for power users that need to customize their figure labels beyond the default cases covered by `draw_labels`.
* And docstrings. Docstrings everywhere!

## Installation

The only prerequisites are Python and ROOT with Python bindings enabled (PyROOT).

* The easiest way to install is through pip:

  ```bash
  pip install cms_figure
  ```

* If for some reason pip cannot be used, please download the source of the desired [release](https://github.com/swang373/cms_figure/releases), unpack it, and install it manually:

  ```bash
  curl -OL https://github.com/swang373/cms_figure/archive/<version>.tar.gz
  tar -zxf <version>.tar.gz
  cd cms_figure-<version>
  python setup.py install
  ```

* If setuptools is not available, then the previously mentioned manual installation won't work. At this point, dropping the cms_figure package into your working directory is a solution, assuming the prerequisites are satisfied.

  ```bash
  curl -OL https://github.com/swang373/cms_figure/archive/<version>.tar.gz
  tar -zxf <version>.tar.gz
  cp -r cms_figure-<version>/cms_figure <working directory>
  ```

To check that the installation succeeded, try running the following lines in a Python interpreter session:

```python
import cms_figure
cms_figure.__version__
```

The correct version number should appear in the terminal .
