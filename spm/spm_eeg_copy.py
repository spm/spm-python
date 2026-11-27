from spm._runtime import Runtime


def spm_eeg_copy(*args, **kwargs):
    r"""
      Copy EEG/MEG data to new files  
        FORMAT D = spm_eeg_copy(S)  
        S           - input struct (optional)  
         fields of S:  
          S.D       - MEEG object or filename of MEEG mat-file  
          S.outfile - filename for the new dataset  
          S.updatehistory - update history information [default: true]  
         
        D           - MEEG object of the new dataset  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_eeg_copy.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_copy", *args, **kwargs)
