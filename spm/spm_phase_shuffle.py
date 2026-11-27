from spm._runtime import Runtime


def spm_phase_shuffle(*args, **kwargs):
    r"""
      Phase-shuffling of a vector  
        FORMAT [y] = spm_phase_shuffle(x,[n])  
        x   - data matrix (time-series in columns)  
        n   - optional window length for windowed shuffling  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_phase_shuffle.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_phase_shuffle", *args, **kwargs)
