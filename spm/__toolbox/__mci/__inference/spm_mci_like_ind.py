from spm.__wrapper__ import Runtime


def spm_mci_like_ind(*args, **kwargs):
    """
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/inference/spm_mci_like_ind.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mci_like_ind", *args, **kwargs)
