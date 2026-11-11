from spm._runtime import Runtime


def spm_vb_Fn(*args, **kwargs):
    r"""
      Compute voxel-wise contributions to model evidence  
        FORMAT [F,L,KL] = spm_vb_Fn(Y,block)  
         
        Y          - [T x N] time series   
        block      - data structure (see spm_vb_glmar)  
         
        F          - [N x 1] vector where nth entry is unique contribution to   
                     model evidence from voxel n  
        L          - [N x 1] Average Likelihood  
        KL.w       - [N x 1] KL w - unique contribution  
        KL.a       - [N x 1] KL a - unique contribution  
        KL.lam     - [N x 1] KL Lambda  
        KL.alpha   - Scalar  
        KL.beta    - Scalar  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_vb_Fn.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_vb_Fn", *args, **kwargs)
