from spm._runtime import Runtime


def spm_samp_mix(*args, **kwargs):
    r"""
      Sample from a Gaussian Mixture PDF  
        FORMAT [x,label] = spm_samp_mix (mix, N)  
         
        mix   Data structure for mixture model (see spm_mix for info)  
        N     Number of samples  
         
        x     [N x d] matrix of samples  
        label [N x 1] vector of sample labels  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mixture/spm_samp_mix.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_samp_mix", *args, **kwargs)
