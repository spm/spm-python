from spm.__wrapper__ import Runtime


def spm_opm_synth_gradiometer(*args, **kwargs):
    """
      Denoise OPM data  
        FORMAT D = spm_opm_synth_gradiometer(S)  
          S               - input structure  
         fields of S:  
          S.D             - SPM MEEG object                       - Default: no Default  
          S.confounds     - n x 1 cell array containing           - Default: REF  
                            channel types(or names:regex allowed)    
          S.derivative    - flag to denoise using derivatives     - Default: 0  
          S.gs            - flag to denoise using global signal   - Default: 0  
          S.prefix        - string prefix for output MEEG object  - Default 'd_'  
          S.lp            -  n x 1 vector of low pass cutoffs     - Default: no filter  
                             (applied to confounds only)                                 
          S.hp            -  n x 1 vector with highpass cutoff    - Default: no filter  
                             (applied to confounds only)  
          S.Y             - m x 1 cell array containing           - Deafualt: 'MEG'   
                            channel types  
        Output:  
          D               - denoised MEEG object (also written to disk)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/MEEGtools/spm_opm_synth_gradiometer.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_opm_synth_gradiometer", *args, **kwargs)
