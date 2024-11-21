from spm.__wrapper__ import Runtime


def spm_eeg_split_conditions(*args, **kwargs):
    """
      Splits a file into different conditions in order to facilitate TF  
        processing. The idea is to create several smaller files, run TF, then  
        aveage within the condition files using spm_eeg_average_tf and lastly,  
        merge again.  
        FORMAT D = spm_eeg_split_conditions(S)  
         
        S        - optional input struct  
        (optional) fields of S:  
        D        - MEEG object or filename of M/EEG mat-file with epoched data  
         
        Output:  
        D        - MEEG object (also written on disk)  
         
        The function also physically removes bad trials.  
         
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/MEEGtools/spm_eeg_split_conditions.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_split_conditions", *args, **kwargs)
