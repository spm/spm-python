from spm.__wrapper__ import Runtime


def spm_eeg_average_TF(*args, **kwargs):
    """
      Average each channel over trials or trial types, for time-frequency data  
        FORMAT D = spm_eeg_average_TF(S)  
         
        S         - optional input struct  
           fields of S:  
        S.D           - MEEG object or filename of M/EEG mat-file with epoched TF data  
        S.circularise - flag that indicates whether average is straight (0) or  
                        vector (1) of phase angles.  
        S.robust      - (optional) - use robust averaging (only for power)  
                        .savew  - save the weights in an additional dataset  
                        .bycondition - compute the weights by condition (1,  
                                       default) or from all trials (0)  
                        .ks     - offset of the weighting function (default: 3)  
        S.trim       - trim mean by a percentile (e.g 10% trim: S.trim=10) default =0  
         
        Output:  
        D         - MEEG object (also written to disk).  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_average_TF.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_average_TF", *args, **kwargs)
