from spm._runtime import Runtime


def spm_cfg_eeg_avgtime(*args, **kwargs):
    """
      Configuration file for averaging over time  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_avgtime.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_cfg_eeg_avgtime", *args, **kwargs)
