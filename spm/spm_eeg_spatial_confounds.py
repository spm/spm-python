from spm._runtime import Runtime


def spm_eeg_spatial_confounds(*args, **kwargs):
    r"""
      This function defines spatial confounds and adds them to MEEG dataset.  
        FORMAT D = spm_eeg_spatial_confounds(S)  
         
        S        - optional input struct  
         fields of S:  
          D        - MEEG object or filename of M/EEG mat-file with epoched data  
          mode     - method for definition of the confounds (EYES, BESA, SVD,  
                     SPMEEG, CLEAR)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_eeg_spatial_confounds.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_spatial_confounds", *args, **kwargs)
