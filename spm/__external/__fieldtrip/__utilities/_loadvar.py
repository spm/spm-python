from spm._runtime import Runtime


def _loadvar(*args, **kwargs):
    r"""
      LOADVAR is a helper function for cfg.inputfile  
         
        See also SAVEVAR  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/utilities/private/loadvar.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("loadvar", *args, **kwargs)
