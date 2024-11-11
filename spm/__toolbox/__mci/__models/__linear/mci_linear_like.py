from spm.__wrapper__ import Runtime


def mci_linear_like(*args, **kwargs):
    """
      Compute log likelihood of linear model  
        FORMAT [L,E,st] = mci_linear_like (theta,M,U,Y)  
         
        theta     regression coefficients  
        M         model  
        U         inputs  
        Y         data  
          
        L         Log likelihood  
        E         Errors  
        st        Status flag (0 for OK, -1 for problem)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/models/linear/mci_linear_like.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mci_linear_like", *args, **kwargs)
