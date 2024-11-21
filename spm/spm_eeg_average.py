from spm.__wrapper__ import Runtime


def spm_eeg_average(*args, **kwargs):
    """
      Average each channel over trials or trial types  
        FORMAT D = spm_eeg_average(S)  
         
        S        - optional input struct  
           fields of S:  
        D        - MEEG object or filename of M/EEG mat-file with epoched data  
        S.robust      - (optional) - use robust averaging  
                        .savew  - save the weights in an additional dataset  
                        .bycondition - compute the weights by condition (1,  
                                       default) or from all trials (0)  
                        .ks     - offset of the weighting function (default: 3)  
        S.trim       - trim mean by a percentile (e.g 10% trim: S.trim=10) default =0  
        S.prefix     - prefix for the output file (default - 'm')  
         
        Output:  
        D        - MEEG object (also written on disk)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_average.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_average", *args, **kwargs)
