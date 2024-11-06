from spm.__wrapper__ import Runtime


def writeCTFMRI(*args, **kwargs):
    """
      Version 1.2   25 April 2007   Module writeCPersist changed, and removed from this text  
                                      file.  
        Version 1.1   19 April 2007 : No changes from v1.0  
        Version 1.0   27 Oct. 2006  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/ctf/writeCTFMRI.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("writeCTFMRI", *args, **kwargs, nargout=0)
