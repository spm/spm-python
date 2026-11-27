from spm._runtime import Runtime


def writeCTFMRI(*args, **kwargs):
    r"""
      Version 1.2   25 April 2007   Module writeCPersist changed, and removed from this text  
                                      file.  
        Version 1.1   19 April 2007 : No changes from v1.0  
        Version 1.0   27 Oct. 2006  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/ctf/writeCTFMRI.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("writeCTFMRI", *args, **kwargs, nargout=0)
