from spm._runtime import Runtime


def _closedf(*args, **kwargs):
    r"""
      EDF=closedf(EDF)  
        Opens an EDF File (European Data Format for Biosignals) into MATLAB  
        <A HREF="http://www.medfac.leidenuniv.nl/neurology/knf/kemp/edf.htm">About EDF</A>   
         
        EDF   struct of EDF-Header of a EDF-File  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/closedf.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("closedf", *args, **kwargs)
