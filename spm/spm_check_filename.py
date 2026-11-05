from spm._runtime import Runtime


def spm_check_filename(*args, **kwargs):
    r"""
      Check paths are valid and try to restore path names  
        FORMAT V = spm_check_filename(V)  
         
        V - struct array of file handles  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_check_filename.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_check_filename", *args, **kwargs)
