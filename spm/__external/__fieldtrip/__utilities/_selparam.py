from spm._runtime import Runtime


def _selparam(*args, **kwargs):
    r"""
      SELPARAM(DATA) extracts the fieldnames param of the structure data containing functional  
        data, which have a dimensionality consistent with the dimord field in the data. Selparam  
        is a helper function to selectdata  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/utilities/private/selparam.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("selparam", *args, **kwargs)
