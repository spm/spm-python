from spm._runtime import Runtime


def _isfunction(*args, **kwargs):
    r"""
      ISFUNCTION tests whether the function of the specified name is a callable  
        function on the current MATLAB path.  
         
        Note that this is *not* equivalent to calling exist(funcname, 'file'),  
        since that will return 7 in case funcname exists as a folder.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/isfunction.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("isfunction", *args, **kwargs)
