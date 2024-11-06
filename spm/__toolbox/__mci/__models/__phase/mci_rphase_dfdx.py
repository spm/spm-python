from spm.__wrapper__ import Runtime


def mci_rphase_dfdx(*args, **kwargs):
    """
      State sensitivity for phase model (reduced connectivity)  
        FORMAT [dfdx] = mci_rphase_dfdx (x,u,P,M)  
         
        x      state vector  
        M      model structure  
        P      parameter vector  
         
        dfdx   Jacobian wrt states  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/models/phase/mci_rphase_dfdx.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mci_rphase_dfdx", *args, **kwargs)
