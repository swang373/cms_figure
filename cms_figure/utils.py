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

from .labels import CMSLabel, LuminosityLabel


def draw_labels(lumi_text, cms_position='left', extra_text=''):
    """Draw the CMS Publication Committee figure labels on the active canvas.

    Parameters
    ----------
    lumi_text : string
        The luminosity label text. Data taking periods must be separated by
        the "+" symbol, e.g. "19.7 fb^{-1} (8 TeV) + 4.9 fb^{-1} (7 TeV)".
    cms_position : string, optional
        The CMS label position on the active canvas:
            :left: The top left corner inside the frame (default)
            :center: The top center inside the frame
            :right: The top right corner inside the frame
            :outside: The top left corner outside the frame
    extra_text : string, optional
        The sublabel text positioned below the CMS label inside of the frame
        or to the right of the CMS label outside of the frame. Common examples
        are "Preliminary", "Simulation", or "Unpublished". The default is an
        empty string for no sublabel.
    """
    cms_label = CMSLabel()
    cms_label.position = cms_position
    cms_label.sublabel.text = extra_text
    cms_label.draw()
    lumi_label = LuminosityLabel(lumi_text)
    lumi_label.draw()
    ROOT.gPad.Update()

