from spm.__wrapper__ import Runtime


def mne_read_noise_cov(*args, **kwargs):
    """
       
        [cov] = mne_read_noise_cov(fname)  
         
        Reads a noise-covariance matrix from a fiff file  
         
        fname      - The name of the file  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/mne_read_noise_cov.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mne_read_noise_cov", *args, **kwargs)
