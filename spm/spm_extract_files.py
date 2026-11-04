from spm._runtime import Runtime


def spm_extract_files(*args, **kwargs):
    r"""
      FORMAT spm_extract_files(P,cwd)  
        forints files (and their subroutines) and expect them to the current  
        directory  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_extract_files.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_extract_files", *args, **kwargs, nargout=0)
