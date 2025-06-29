from spm._runtime import Runtime


def spm_eeg_reduce_cva(*args, **kwargs):
    """
      Plugin for data reduction using PCA  
        FORMAT res = spm_eeg_reduce_cva(S)  
         
        S                     - input structure  
        fields of S:  
           S.ncomp            - number of PCA components  
         
        Output:  
         res -  
          If no input is provided the plugin returns a cfg branch for itself  
         
          If input is provided:  
             montage struct implementing projection to PCA subspace  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_reduce_cva.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_reduce_cva", *args, **kwargs)
