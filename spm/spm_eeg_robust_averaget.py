from spm._runtime import Runtime


def spm_eeg_robust_averaget(*args, **kwargs):
    r"""
      Apply robust averaging routine to data sets   
        FORMAT [B,Wf] = spm_eeg_robust_averaget(data,ks)  
        data   - data matrix to be averaged  
        ks     - offset of the weighting function (default: 3)  
         
        Wf     - estimated weights  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_eeg_robust_averaget.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_robust_averaget", *args, **kwargs)
