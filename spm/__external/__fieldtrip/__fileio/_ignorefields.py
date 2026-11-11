from spm._runtime import Runtime


def _ignorefields(*args, **kwargs):
    r"""
      IGNOREFIELDS returns a list of fields that can be present in the cfg structure that  
        should be ignored at various places in the code, e.g. for provenance, history,  
        size-checking, etc.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/ignorefields.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ignorefields", *args, **kwargs)
