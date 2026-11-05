from spm._runtime import Runtime


def spm_mci_adjoint_int(*args, **kwargs):
    r"""
      Integrate adjoint equation  
        FORMAT [lambda] = spm_mci_adjoint_int (U,P,M,V,djdx,tol)  
         
        U         Inputs  
        P         Parameters  
        M         Model structure  
        V         states  
        djdx      derivative of log likelihood wrt states  
        tol       tolerances  
         
        lambda    adjoint parameters, at times M.t  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mci/gradients/spm_mci_adjoint_int.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mci_adjoint_int", *args, **kwargs)
