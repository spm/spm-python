from spm.__wrapper__ import Runtime


def spm_ker2coh(*args, **kwargs):
    """
      computes coherence from kernels  
        FORMAT [coh,fsd] = spm_ker2coh(ker,pst))  
         
        ker  - first-order (Volterra) kernels  
        pst  - time samples  
         
        coh  - coherence  
        fsd  - frequency specific delay (seconds)   
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/spectral/spm_ker2coh.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_ker2coh", *args, **kwargs)
