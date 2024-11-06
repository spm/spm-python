from spm.__wrapper__ import Runtime


def spm_unlink(*args, **kwargs):
    """
      Silently delete files on disk - a compiled routine  
        FORMAT spm_unlink('file1','file2','file3','file4',...)  
         
        Remove the specified file(s) using a system call to unlink().  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_unlink.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_unlink", *args, **kwargs, nargout=0)
