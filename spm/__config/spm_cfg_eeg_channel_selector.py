from spm.__wrapper__ import Runtime


def spm_cfg_eeg_channel_selector(*args, **kwargs):
    """
      Generic M/EEG channel selector based on label and type  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_channel_selector.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_cfg_eeg_channel_selector", *args, **kwargs)
