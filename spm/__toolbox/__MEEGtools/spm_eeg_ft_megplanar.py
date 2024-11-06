from spm.__wrapper__ import Runtime


def spm_eeg_ft_megplanar(*args, **kwargs):
    """
      Function for transforming MEG data to planar gradient  
         
        FORMAT  D = spm_eeg_ft_megplanar(S)  
         
        S           - input structure (optional)  
        (optional) fields of S:  
          S.D       - filename, or M/EEG object  
          S.prefix  - prefix (default L)  
         
        Output  
          D - dataset converted to planar gradient  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/MEEGtools/spm_eeg_ft_megplanar.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_ft_megplanar", *args, **kwargs)
