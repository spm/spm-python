from spm._runtime import Runtime


def spm_ker2ccf(*args, **kwargs):
    r"""
      computes cross covariance function from kernels  
        FORMAT [ccf,pst] = spm_ker2ccf(ker,dt)  
         
        ker  - first-order (Volterra) kernels  
        dt   - time bin (sec)  
         
        ccf  - cross covariance functions  
        pst  - time samples  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/spectral/spm_ker2ccf.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_ker2ccf", *args, **kwargs)
