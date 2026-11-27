from spm._runtime import Runtime


def spm_eeg_reduce_whiten(*args, **kwargs):
    r"""
      Plugin for data whitening  
        FORMAT res = spm_eeg_reduce_pca(S)  
         
        S                     - input structure  
        fields of S:  
           S.ncomp            - number of PCA components  
         
        Output:  
         res -  
          If no input is provided the plugin returns a cfg branch for itself  
         
          If input is provided:  
             montage struct implementing data whitening  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_eeg_reduce_whiten.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_reduce_whiten", *args, **kwargs)
