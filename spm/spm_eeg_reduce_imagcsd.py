from spm._runtime import Runtime


def spm_eeg_reduce_imagcsd(*args, **kwargs):
    r"""
      Plugin for data reduction based on the imaginary part of CSD  
        with a reference chhannel  
        FORMAT res = spm_eeg_reduce_imagcsd(S)  
         
        S                     - input structure  
        fields of S:  
            
         
        Output:  
         res -  
          If no input is provided the plugin returns a cfg branch for itself  
         
          If input is provided:  
             montage struct implementing projection to PCA subspace  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_eeg_reduce_imagcsd.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_reduce_imagcsd", *args, **kwargs)
