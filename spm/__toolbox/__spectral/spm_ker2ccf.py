from spm.__wrapper__ import Runtime


def spm_ker2ccf(*args, **kwargs):
    """
      computes cross covariance function from kernels  
        FORMAT [ccf,pst] = spm_ker2ccf(ker,dt)  
         
        ker  - first-order (Volterra) kernels  
        dt   - time bin (sec)  
         
        ccf  - cross covariance functions  
        pst  - time samples  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/spectral/spm_ker2ccf.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_ker2ccf", *args, **kwargs)
