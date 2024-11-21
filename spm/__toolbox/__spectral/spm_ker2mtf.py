from spm.__wrapper__ import Runtime


def spm_ker2mtf(*args, **kwargs):
    """
      computes modulation transfer function from kernels  
        FORMAT [mtf,Hz] = spm_ker2mtf(ker,dt)  
         
        ker  - first-order (Volterra) kernels  
        dt   - time bin  
         
        mtf  - modulation transfer function  
        Hz   - frequencies  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/spectral/spm_ker2mtf.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_ker2mtf", *args, **kwargs)
