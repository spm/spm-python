from spm.__wrapper__ import Runtime


def spm_eeg_crop(*args, **kwargs):
    """
      Reduce the data size by cutting in time and frequency  
        FORMAT D = spm_eeg_crop(S)  
         
        S        - optional input struct  
         fields of S:  
          D        - MEEG object or filename of M/EEG mat-file with epoched data  
          timewin  - time window to retain {in PST ms}  
          freqwin  - frequency window to retain  
          channels - cell array of channel labels or 'all' [default]  
          prefix   - prefix for the output file [default: 'p']  
         
        Output:  
        D        - MEEG object (also written on disk)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_crop.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_crop", *args, **kwargs)
