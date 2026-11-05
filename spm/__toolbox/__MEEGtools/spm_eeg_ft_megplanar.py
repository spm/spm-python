from spm._runtime import Runtime


def spm_eeg_ft_megplanar(*args, **kwargs):
    r"""
      Function for transforming MEG data to planar gradient  
         
        FORMAT  D = spm_eeg_ft_megplanar(S)  
         
        S           - input structure (optional)  
        (optional) fields of S:  
          S.D       - filename, or M/EEG object  
          S.prefix  - prefix (default L)  
         
        Output  
          D - dataset converted to planar gradient  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/MEEGtools/spm_eeg_ft_megplanar.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_ft_megplanar", *args, **kwargs)
