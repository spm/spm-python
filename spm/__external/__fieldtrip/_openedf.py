from mpython import Runtime


def _openedf(*args, **kwargs):
    """
      EDF=openedf(FILENAME)
        Opens an EDF File (European Data Format for Biosignals) in MATLAB (R)
        <A HREF="http://www.medfac.leidenuniv.nl/neurology/knf/kemp/edf.htm">About EDF</A>


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/openedf.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("openedf", *args, **kwargs)
