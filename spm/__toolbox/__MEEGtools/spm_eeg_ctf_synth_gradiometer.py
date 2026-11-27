from spm._runtime import Runtime


def spm_eeg_ctf_synth_gradiometer(*args, **kwargs):
    r"""
      Apply CTF synthetic gradiometry to MEG data  
        FORMAT D = spm_opm_synth_gradiometer(S)  
          S               - input structure  
         fields of S:  
          S.D             - SPM MEEG object or string to path     - Default: no Default  
          S.gradient      - Integer ranging from 0-3 defining  
                            order of gradiometry                  - Default: 3  
          S.method        - string of package to perform  
                            gradiometry correction                - Default: 'fieldtrip'  
          S.prefix        - string prefix for output MEEG object  - Default: 'g_'  
        Output:  
          D               - denoised MEEG object (also written to disk)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/MEEGtools/spm_eeg_ctf_synth_gradiometer.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_ctf_synth_gradiometer", *args, **kwargs)
