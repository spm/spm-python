from spm._runtime import Runtime


def spm_authors(*args, **kwargs):
    r"""
      Return list of SPM coauthors  
        FORMAT [current, previous] = spm_authors  
        current  - cell array of SPM coauthors of the current release  
        previous - cell array of SPM coauthors of previous releases  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_authors.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_authors", *args, **kwargs)
