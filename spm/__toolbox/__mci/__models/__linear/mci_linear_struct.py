from spm.__wrapper__ import Runtime


def mci_linear_struct(*args, **kwargs):
    """
      Set up data structures for linear model  
        FORMAT [M,U,Xfull] = mci_linear_struct (Nobs,lambda,des)  
         
        Nobs      number of data points  
        lambda    noise precision  
        des       type of design   
         
        M         model structure  
        U         U.X is the design matrix  
        Xfull     Design matrix for data points [1:T]  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/models/linear/mci_linear_struct.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mci_linear_struct", *args, **kwargs)
