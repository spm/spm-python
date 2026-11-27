from spm._runtime import Runtime


def spm_eeg_bc(*args, **kwargs):
    r"""
      'Baseline Correction' for M/EEG data  
        FORMAT D = spm_eeg_bc(S)  
         
        S        - optional input struct  
             fields of S:  
          S.D       - MEEG object or filename of M/EEG mat-file with epoched data  
          S.timewin - 2-element vector with start and end of baseline period {ms}  
                      [default: the negative times if present or the whole trial  
                      otherwise]  
          S.save    - save the baseline corrected data in a separate file [default: true]  
          S.updatehistory - update history information [default: true]  
          S.prefix     - prefix for the output file [default: 'b']  
         
        D        - MEEG object (also saved on disk if requested)  
       __________________________________________________________________________  
         
        Subtract average baseline from all M/EEG and EOG channels  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_eeg_bc.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_bc", *args, **kwargs)
