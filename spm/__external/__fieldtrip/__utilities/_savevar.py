from spm._runtime import Runtime


def _savevar(*args, **kwargs):
    r"""
      SAVEVAR is a helper function for cfg.outputfile  
         
        See also LOADVAR  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/utilities/private/savevar.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("savevar", *args, **kwargs, nargout=0)
