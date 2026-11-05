from spm._runtime import Runtime


def spm_ker2coh(*args, **kwargs):
    r"""
      computes coherence from kernels  
        FORMAT [coh,fsd] = spm_ker2coh(ker,pst))  
         
        ker  - first-order (Volterra) kernels  
        pst  - time samples  
         
        coh  - coherence  
        fsd  - frequency specific delay (seconds)   
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/spectral/spm_ker2coh.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_ker2coh", *args, **kwargs)
