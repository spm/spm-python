from spm._runtime import Runtime


def mci_linsqr_struct(*args, **kwargs):
    r"""
      Set up data structures for linsqr model  
        FORMAT [M,U,Xfull] = mci_linsqr_struct (Nobs,lambda,des)  
         
        Nobs      number of data points  
        lambda    noise precision  
        des       type of design   
         
        M         model structure  
        U         U.X is the design matrix  
        Xfull     Design matrix for data points [1:T]  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mci/models/linsqr/mci_linsqr_struct.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mci_linsqr_struct", *args, **kwargs)
