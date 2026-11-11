from spm._runtime import Runtime


def mne_read_cov(*args, **kwargs):
    r"""
       
        [cov] = mne_read_cov(fid,node,kind)  
         
        Reads a covariance matrix from a fiff file  
         
        fid       - an open file descriptor  
        node      - look for the matrix in here  
        cov_kind  - what kind of a covariance matrix do we want?  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/mne_read_cov.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mne_read_cov", *args, **kwargs)
