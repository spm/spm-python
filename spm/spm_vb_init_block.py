from spm._runtime import Runtime


def spm_vb_init_block(*args, **kwargs):
    r"""
      Initialise Variational Bayes for GLM-AR models  
        FORMAT [block] = spm_vb_init_block(Y,block)  
         
        Y      - [T x N] time series with T time points, N voxels  
        block  - data structure (see spm_vb_glmar)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_vb_init_block.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_vb_init_block", *args, **kwargs)
