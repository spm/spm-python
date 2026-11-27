from spm._runtime import Runtime


def spm_ker2csd(*args, **kwargs):
    r"""
      computes cross spectral density from kernels  
        FORMAT [csd,Hz] = spm_ker2csd(ker,pst)  
         
        ker  - first-order (Volterra) kernels  
        pst  - time samples  
         
        csd  - cross spectral density  
        Hz   - frequencies  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/spectral/spm_ker2csd.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_ker2csd", *args, **kwargs)
