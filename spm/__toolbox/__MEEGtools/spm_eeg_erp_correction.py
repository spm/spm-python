from spm.__wrapper__ import Runtime


def spm_eeg_erp_correction(*args, **kwargs):
    """
      Applies corrections to ERPs or single trials as in DCM-ERP  
        This can be used to make a sensor level analysis or source reconstruction  
        consistent with DCM.  
        FORMAT D = spm_eeg_erp_correction(S)  
         
        S        - optional input struct  
        (optional) fields of S:  
        S.D        - MEEG object or filename of M/EEG mat-file with epoched data  
        S.detrend  - detrending order (0 for no detrending)  
        S.hanning  - apply Hanning window (true or false)  
        S.chtype   - channel type (default 'MEEG')  
         
        Output:  
        D        - MEEG object (also written on disk)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/MEEGtools/spm_eeg_erp_correction.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_erp_correction", *args, **kwargs)
