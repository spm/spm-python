from spm._runtime import Runtime


def mci_linsqr_gen(*args, **kwargs):
    r"""
      Output of linear model with squared params  
        FORMAT [y] = mci_linsqr_gen (theta,M,U)  
         
        theta     regression coefficients  
        M         model structure  
        U         U.X contains design matrix  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mci/models/linsqr/mci_linsqr_gen.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mci_linsqr_gen", *args, **kwargs)
