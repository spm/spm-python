from spm._runtime import Runtime


def mne_pick_channels_cov(*args, **kwargs):
    r"""
       
        [cov] = mne_pick_channels_cov(orig,include,exclude)  
         
        Pick desired channels from a covariance matrix  
         
        orig      - The original covariance matrix  
        include   - Channels to include (if empty, include all available)  
        exclude   - Channels to exclude (if empty, do not exclude any)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/mne_pick_channels_cov.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mne_pick_channels_cov", *args, **kwargs)
