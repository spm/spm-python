from spm.__wrapper__ import Runtime


def mci_linsqr_struct(*args, **kwargs):
    """
      Set up data structures for linsqr model  
        FORMAT [M,U,Xfull] = mci_linsqr_struct (Nobs,lambda,des)  
         
        Nobs      number of data points  
        lambda    noise precision  
        des       type of design   
         
        M         model structure  
        U         U.X is the design matrix  
        Xfull     Design matrix for data points [1:T]  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/models/linsqr/mci_linsqr_struct.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mci_linsqr_struct", *args, **kwargs)
