from spm.__wrapper__ import Runtime


def ft_trialfun_emgdetect(*args, **kwargs):
    """
      Note that there are some parameters, like the EMG channel name and the  
        processing that is done on the EMG channel data, which are hardcoded in  
        this trial function. You should change these parameters if necessary.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/trialfun/ft_trialfun_emgdetect.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_trialfun_emgdetect", *args, **kwargs)
