from spm._runtime import Runtime


def ft_trialfun_emgdetect(*args, **kwargs):
    r"""
      Note that there are some parameters, like the EMG channel name and the  
        processing that is done on the EMG channel data, which are hardcoded in  
        this trial function. You should change these parameters if necessary.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/trialfun/ft_trialfun_emgdetect.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_trialfun_emgdetect", *args, **kwargs)
