from spm._runtime import Runtime


def mne_read_noise_cov(*args, **kwargs):
    r"""
       
        [cov] = mne_read_noise_cov(fname)  
         
        Reads a noise-covariance matrix from a fiff file  
         
        fname      - The name of the file  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/mne_read_noise_cov.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mne_read_noise_cov", *args, **kwargs)
