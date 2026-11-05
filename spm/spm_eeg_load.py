from spm._runtime import Runtime


def spm_eeg_load(*args, **kwargs):
    r"""
      Load an M/EEG file in SPM format  
        FORMAT D = spm_eeg_load(P)  
         
        P        - filename of M/EEG file  
        D        - MEEG object   
       __________________________________________________________________________  
          
        spm_eeg_load loads an M/EEG file using the SPM MEEG format. Importantly,  
        the data array is memory-mapped and the struct is converted to MEEG object.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_eeg_load.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_load", *args, **kwargs)
