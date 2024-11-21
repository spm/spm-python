from spm.__wrapper__ import Runtime


def spm_eeg_reref_eeg(*args, **kwargs):
    """
      Rereference EEG data to new reference channel(s)  
        FORMAT [D, S] = spm_eeg_reref_eeg(S)  
         
        S                    - input structure (optional)  
        (optional) fields of S:  
          S.D                - MEEG object or filename of M/EEG mat-file  
          S.refchan          - New reference channel indices or labels  
                               ('average' can be used as shortcut)  
         
        Output:  
        D                    - MEEG object (also written on disk)  
        S                    - record of parameters, including montage  
       __________________________________________________________________________  
         
        spm_eeg_reref_eeg re-references any EEG data within an MEEG dataset, by  
        calling spm_eeg_montage with appropriate montage, excluding bad channels  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/MEEGtools/spm_eeg_reref_eeg.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_reref_eeg", *args, **kwargs)
