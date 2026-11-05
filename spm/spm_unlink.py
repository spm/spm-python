from spm._runtime import Runtime


def spm_unlink(*args, **kwargs):
    r"""
      Silently delete files on disk - a compiled routine  
        FORMAT spm_unlink('file1','file2','file3','file4',...)  
         
        Remove the specified file(s) using a system call to unlink().  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_unlink.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_unlink", *args, **kwargs, nargout=0)
