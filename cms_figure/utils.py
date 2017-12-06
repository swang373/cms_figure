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

