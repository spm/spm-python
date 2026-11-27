from spm._runtime import Runtime


def spm_ker2mtf(*args, **kwargs):
    r"""
      computes modulation transfer function from kernels  
        FORMAT [mtf,Hz] = spm_ker2mtf(ker,dt)  
         
        ker  - first-order (Volterra) kernels  
        dt   - time bin  
         
        mtf  - modulation transfer function  
        Hz   - frequencies  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/spectral/spm_ker2mtf.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_ker2mtf", *args, **kwargs)
