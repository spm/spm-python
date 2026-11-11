from spm._runtime import Runtime


def spm_mkdir(*args, **kwargs):
    r"""
      Make new directory trees  
        FORMAT sts = spm_mkdir(dir,...)  
        dir    - character array, or cell array of strings  
         
        sts    - true if all directories were successfully created or already  
                 existing, false otherwise.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_mkdir.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mkdir", *args, **kwargs)
