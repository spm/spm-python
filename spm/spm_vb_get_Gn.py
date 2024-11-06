from spm.__wrapper__ import Runtime


def spm_vb_get_Gn(*args, **kwargs):
    """
      Compute Gn for VB-GLM-AR modelling   
        FORMAT [G,G1,G2,G3] = spm_vb_get_Gn(Y,slice,n)  
         
        Y      - [T x N] time series   
        slice  - data structure (see spm_vb_glmar)   
        n      - voxel number  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_vb_get_Gn.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_vb_get_Gn", *args, **kwargs)
