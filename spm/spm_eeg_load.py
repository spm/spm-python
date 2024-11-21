from spm.__wrapper__ import Runtime


def spm_eeg_load(*args, **kwargs):
    """
      Load an M/EEG file in SPM format  
        FORMAT D = spm_eeg_load(P)  
         
        P        - filename of M/EEG file  
        D        - MEEG object   
       __________________________________________________________________________  
          
        spm_eeg_load loads an M/EEG file using the SPM MEEG format. Importantly,  
        the data array is memory-mapped and the struct is converted to MEEG object.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_load.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_load", *args, **kwargs)
