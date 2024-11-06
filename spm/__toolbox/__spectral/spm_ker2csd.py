from spm.__wrapper__ import Runtime


def spm_ker2csd(*args, **kwargs):
    """
      computes cross spectral density from kernels  
        FORMAT [csd,Hz] = spm_ker2csd(ker,pst)  
         
        ker  - first-order (Volterra) kernels  
        pst  - time samples  
         
        csd  - cross spectral density  
        Hz   - frequencies  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/spectral/spm_ker2csd.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_ker2csd", *args, **kwargs)
