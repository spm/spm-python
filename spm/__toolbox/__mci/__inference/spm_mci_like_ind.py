from spm._runtime import Runtime


def spm_mci_like_ind(*args, **kwargs):
    r"""
      Compute likelihood wrt selected time points  
        FORMAT [L,e] = spm_mci_like_ind (P,R,M,U,Y)  
         
        P         Flow parameters  
        R         Initial state parameters  
        M         Model structure  
        U         Inputs  [Nin x N]  
        Y         data  
              
        L         Log likelihood  
        e         Prediction errors  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mci/inference/spm_mci_like_ind.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mci_like_ind", *args, **kwargs)
