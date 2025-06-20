from spm._runtime import Runtime


def mci_linsqr_gen(*args, **kwargs):
    """
      Output of linear model with squared params  
        FORMAT [y] = mci_linsqr_gen (theta,M,U)  
         
        theta     regression coefficients  
        M         model structure  
        U         U.X contains design matrix  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/models/linsqr/mci_linsqr_gen.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mci_linsqr_gen", *args, **kwargs)
