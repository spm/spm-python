from spm.__wrapper__ import Runtime


def spm_eeg_robust_averaget(*args, **kwargs):
    """
      Apply robust averaging routine to data sets   
        FORMAT [B,Wf] = spm_eeg_robust_averaget(data,ks)  
        data   - data matrix to be averaged  
        ks     - offset of the weighting function (default: 3)  
         
        Wf     - estimated weights  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_robust_averaget.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_robust_averaget", *args, **kwargs)
