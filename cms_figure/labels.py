# MIT License
# 
# Copyright (c) 2017 Sean-Jiun Wang
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import ROOT


class LabelTextAlignmentError(Exception):
    pass


class LabelPositionError(Exception):
    pass


class LabelBase(ROOT.TLatex):
    """The base label class."""

    # Tuples of horizontal and vertical text alignment names and
    # their corresponding ROOT text alignment integer values.
    TEXT_ALIGNMENT = {
        ('left', 'bottom'): 11,
        ('left', 'center'): 12,
        ('left', 'top'): 13,
        ('center', 'bottom'): 21,
        ('center', 'center'): 22,
        ('center', 'top'): 23,
        ('right', 'bottom'): 31,
        ('right', 'center'): 32,
        ('right', 'top'): 33,
    }

    def __init__(self):
        super(LabelBase, self).__init__()

    @property
    def align(self):
        return self.GetTextAlign()

    @align.setter
    def align(self, value):
        if value in self.TEXT_ALIGNMENT:
            self.SetTextAlign(self.TEXT_ALIGNMENT[value])
        elif value in self.TEXT_ALIGNMENT.values():
            self.SetTextAlign(value)
        else:
            raise LabelTextAlignmentError('Unrecognized value: {0!s}'.format(value))

    @property
    def font(self):
        return self.GetTextFont()

    @font.setter
    def font(self, value):
        self.SetTextFont(value)

    @property
    def size(self):
        return self.GetTextSize()

    @size.setter
    def size(self, value):
        self.SetTextSize(value)

    @staticmethod
    def get_canvas_margins():
        """Return the top, right, bottom, and left margins of the active canvas.

        Figure labels are often oriented relative to these margins.
        """
        return ROOT.gPad.GetTopMargin(), ROOT.gPad.GetRightMargin(), ROOT.gPad.GetBottomMargin(), ROOT.gPad.GetLeftMargin()


class CMSLabel(LabelBase):
    """A label displaying the CMS name.

    Credits to Gautier Hamel de Monchenault (Saclay), Joshua Hardenbrook (Princeton),
    and Dinko Ferencek (Rutgers) for the initial Python implementation.

    The label's text and style properties, which are set to default values from the
    CMS Publication Committee, are exposed as instance attributes for customization:

    text : string
        The CMS label text. The default is "CMS".
    position : string
        One of the following label positions on the active canvas:
            :left: The top left corner inside the frame (default)
            :center: The top center inside the frame
            :right: The top right corner inside the frame
            :outside: The top left corner outside the frame
    font : int
        The text font code. The default is 61 (Helvetica Bold).
    scale : float
        The text size scale relative to the size of the top margin
        of the active canvas. The default is 0.75.
    padding_left : float
        The amount of padding to the left of the text when positioned
        inside the frame, relative to the frame width of the active canvas.
        The default is 0.045.
    padding_right : float
        The amount of padding to the right of the text when positioned
        inside the frame, relative to the frame width of the active canvas.
        The default is 0.045.
    padding_top : float
        The amount of padding above the text. When positioned inside of
        the frame, it is relative to the frame height of the active canvas
        and the default is 0.035. When positioned outside of the frame, it
        is relative to the size of the top margin of the active canvas and
        the default is 0.8.
    sublabel.text : string
        The sublabel text positioned below the main text inside of the frame
        or to the right of the main text outside of the frame. Common examples
        are "Preliminary", "Simulation", or "Unpublished". The default is an
        empty string for no sublabel.
    sublabel.font : string
        The sublabel text font code. The default is 52 (Helvetica Italic).
    sublabel.scale : float
        The sublabel text size scale relative to the size of the main text.
        The default is 0.76.
    sublabel.padding_left : float
        The amount of padding to the left of the sublabel text relative to the
        frame width of the active canvas. This only applies if the main text is
        positioned outside the frame of the active canvas. The default is 0.12.
    sublabel.padding_top : float
        The amount of padding above the sublabel text relative to the size of
        the main text. This only applies if the main text is positioned inside
        the frame of the active canvas. The default is 1.2.
    """
    def __init__(self):
        super(CMSLabel, self).__init__()
        self.text = 'CMS'
        self.position = 'left'
        self.font = 61
        self.scale = 0.75
        self.padding_left = 0.045
        self.padding_right = 0.045
        self.padding_top = None
        self.sublabel = LabelBase()
        self.sublabel.text = ''
        self.sublabel.font = 52
        self.sublabel.scale = 0.76
        self.sublabel.padding_left = 0.12
        self.sublabel.padding_top = 1.2

    def draw(self):
        """Draw the CMS label and sublabel on the active canvas."""
        # Draw the label.
        if self.position == 'left':
            label_coordinates = self._draw_label_left()
        elif self.position == 'center':
            label_coordinates = self._draw_label_center()
        elif self.position == 'right':
            label_coordinates = self._draw_label_right()
        elif self.position == 'outside':
            label_coordinates = self._draw_label_outside()
        else:
            raise LabelPositionError('Unrecognized value: {0}'.format(self.position))
        # Draw the sublabel.
        if self.sublabel.text:
            if self.position == 'outside':
                self._draw_sublabel_outside(*label_coordinates)
            else:
                self._draw_sublabel_inside(*label_coordinates)

    def _draw_label_left(self):
        """Draw the label on the top left corner inside the frame and return its coordinates."""
        top_margin, right_margin, bottom_margin, left_margin = self.get_canvas_margins()
        self.size = self.scale * top_margin
        self.align = ('left', 'top')
        x = left_margin + self.padding_left * (1 - left_margin - right_margin)
        y = 1 - top_margin - (self.padding_top or 0.035) * (1 - top_margin - bottom_margin)
        self.DrawLatexNDC(x, y, self.text)
        return x, y

    def _draw_label_center(self):
        """Draw the label on the top center inside the frame and return its coordinates."""
        top_margin, right_margin, bottom_margin, left_margin = self.get_canvas_margins()
        self.size = self.scale * top_margin
        self.align = ('center', 'top')
        x = left_margin + 0.5 * (1 - left_margin - right_margin)
        y = 1 - top_margin - (self.padding_top or 0.035) * (1 - top_margin - bottom_margin)
        self.DrawLatexNDC(x, y, self.text)
        return x, y

    def _draw_label_right(self):
        """Draw the label on the top right corner inside the frame and return its coordinates."""
        top_margin, right_margin, bottom_margin, left_margin = self.get_canvas_margins()
        self.size = self.scale * top_margin
        self.align = ('right', 'top')
        x = 1 - right_margin - self.padding_right * (1 - left_margin - right_margin)
        y = 1 - top_margin - (self.padding_top or 0.035) * (1 - top_margin - bottom_margin)
        self.DrawLatexNDC(x, y, self.text)
        return x, y

    def _draw_label_outside(self):
        """Draw the label on the top left corner outside the frame and return its coordinates."""
        top_margin, _, _, left_margin = self.get_canvas_margins()
        self.size = self.scale * top_margin
        self.align = ('left', 'bottom')
        x = left_margin
        y = 1 - (self.padding_top or 0.8) * top_margin
        self.DrawLatexNDC(x, y, self.text)
        return x, y

    def _draw_sublabel_inside(self, x_label, y_label):
        """Draw the sublabel below the label inside the frame."""
        self.sublabel.size = self.sublabel.scale * self.size
        self.sublabel.align = self.align
        x_sublabel = x_label
        y_sublabel = y_label - self.sublabel.padding_top * self.size
        self.sublabel.DrawLatexNDC(x_sublabel, y_sublabel, self.sublabel.text)

    def _draw_sublabel_outside(self, x_label, y_label):
        """Draw the sublabel to the right of the label outside the frame."""
        _, right_margin, _, left_margin = self.get_canvas_margins()
        self.sublabel.size = self.sublabel.scale * self.size
        self.sublabel.align = self.align
        x_sublabel = left_margin + self.sublabel.padding_left * (1 - left_margin - right_margin)
        y_sublabel = y_label
        self.sublabel.DrawLatexNDC(x_sublabel, y_sublabel, self.sublabel.text)


class LuminosityLabel(LabelBase):
    """A label displaying the integrated luminosity and center-of-mass energy.

    Credits to Gautier Hamel de Monchenault (Saclay), Joshua Hardenbrook (Princeton),
    and Dinko Ferencek (Rutgers) for the initial Python implementation.

    The label's text and style properties, which are set to default values from the
    CMS Publication Committee, are exposed as instance attributes for customization:

    font : int
        The text font code. The default is 42 (Helvetica).
    scale : float
        The text size scale relative to the size of the top margin
        of the active canvas. The default is 0.6.
    align : int or 2-tuple of strings
        The text alignment relative to the drawing coordinates of the text as
        either an integer code or tuple of horizontal and vertical alignment
        names, respectively. The default is 31, or ("right", "bottom").
    padding_top : float
        The amount of padding above the text relative to the size
        of the top margin of the active canvas. The default is 0.8.

    Parameters
    ----------
    text : string
        The luminosity label text. Data taking periods must be separated by
        the "+" symbol, e.g. "19.7 fb^{-1} (8 TeV) + 4.9 fb^{-1} (7 TeV)".
    """
    def __init__(self, text):
        super(LuminosityLabel, self).__init__()
        self.text = text
        self.font = 42
        self.scale = 0.6
        self.align = 31
        self.padding_top = 0.8

    def draw(self):
        """Draw the luminosity label on the active canvas."""
        top_margin, right_margin, _, _ = self.get_canvas_margins()
        self.size = self.scale * top_margin
        x = 1 - right_margin
        y = 1 - self.padding_top * top_margin
        self.DrawLatexNDC(x, y, self.text)

