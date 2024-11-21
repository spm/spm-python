from spm.__wrapper__ import Runtime


def _isfunction(*args, **kwargs):
    """
      ISFUNCTION tests whether the function of the specified name is a callable  
        function on the current MATLAB path.  
         
        Note that this is *not* equivalent to calling exist(funcname, 'file'),  
        since that will return 7 in case funcname exists as a folder.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/isfunction.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("isfunction", *args, **kwargs)
