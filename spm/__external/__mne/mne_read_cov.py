from spm.__wrapper__ import Runtime


def mne_read_cov(*args, **kwargs):
    """
       
        [cov] = mne_read_cov(fid,node,kind)  
         
        Reads a covariance matrix from a fiff file  
         
        fid       - an open file descriptor  
        node      - look for the matrix in here  
        cov_kind  - what kind of a covariance matrix do we want?  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/mne_read_cov.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mne_read_cov", *args, **kwargs)
