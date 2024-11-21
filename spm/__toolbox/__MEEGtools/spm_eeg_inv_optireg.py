from spm.__wrapper__ import Runtime


def spm_eeg_inv_optireg(*args, **kwargs):
    """
      D = spm_eeg_inv_optireg(S)  
        Registers a template anatomical to SPM M/EEG dataset, using the fiducial  
        information obtained from an optical scanning system at the FIL, as a  
        part of MEG data collection from Apr 2021.  
         
        Input:  
         
        S  - input struct  
        fields of S:  
         
        S.D       - SPM MEEG object                           (REQUIRED)  
        S.fidfile - path to .csv file with subject anatomical fidicals and coil  
                       locations                              (REQUIRED)  
        S.save    - logical to save registration in current dataset  
                                                              (default: TRUE)  
        S.forward - calles the forward modelling ui after registration  
                                                              (default: FALSE)  
         
        Output:  
         
        D - Coregistered dataset.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/MEEGtools/spm_eeg_inv_optireg.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_inv_optireg", *args, **kwargs)
