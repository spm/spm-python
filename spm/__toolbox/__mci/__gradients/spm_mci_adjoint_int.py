from spm.__wrapper__ import Runtime


def spm_mci_adjoint_int(*args, **kwargs):
    """
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/gradients/spm_mci_adjoint_int.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mci_adjoint_int", *args, **kwargs)
