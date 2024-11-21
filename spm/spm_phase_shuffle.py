from spm.__wrapper__ import Runtime


def spm_phase_shuffle(*args, **kwargs):
    """
      Phase-shuffling of a vector  
        FORMAT [y] = spm_phase_shuffle(x,[n])  
        x   - data matrix (time-series in columns)  
        n   - optional window length for windowed shuffling  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_phase_shuffle.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_phase_shuffle", *args, **kwargs)
