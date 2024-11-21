from spm.__wrapper__ import Runtime


def spm_eeg_copy(*args, **kwargs):
    """
      Copy EEG/MEG data to new files  
        FORMAT D = spm_eeg_copy(S)  
        S           - input struct (optional)  
         fields of S:  
          S.D       - MEEG object or filename of MEEG mat-file  
          S.outfile - filename for the new dataset  
          S.updatehistory - update history information [default: true]  
         
        D           - MEEG object of the new dataset  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_copy.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_copy", *args, **kwargs)
