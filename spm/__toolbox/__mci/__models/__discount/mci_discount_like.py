from spm.__wrapper__ import Runtime


def mci_discount_like(*args, **kwargs):
    """
      Compute log likelihood of discount model  
        FORMAT [L,E,st] = mci_discount_like (P,M,U,Y)  
         
        P         parameters  
        M         model  
        U         inputs  
        Y         data  
          
        L         Log likelihood  
        E         Errors  
        st        Status flag (0 for OK, -1 for problem)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/models/discount/mci_discount_like.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mci_discount_like", *args, **kwargs)
