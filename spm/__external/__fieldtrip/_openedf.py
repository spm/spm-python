from spm._runtime import Runtime


def _openedf(*args, **kwargs):
    r"""
      EDF=openedf(FILENAME)  
        Opens an EDF File (European Data Format for Biosignals) in MATLAB (R)  
        <A HREF="http://www.medfac.leidenuniv.nl/neurology/knf/kemp/edf.htm">About EDF</A>  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/openedf.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("openedf", *args, **kwargs)
