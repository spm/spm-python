from spm.__wrapper__ import Runtime


def mci_lds_fx(*args, **kwargs):
    """
      Flow for linear system, dx/dt=Ax, with constrained connectivity  
        FORMAT [f,A,Pt] = mci_lds_fx (x,u,P,M)  
         
        x     State vector  
        u     input  
        P     parameters (vectorised)  
        M     model structure  
         
        f     Flow, dx/dt  
        A     f=Ax  
        Pt    Parameters (transformed from latent pars)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/models/lds/mci_lds_fx.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mci_lds_fx", *args, **kwargs)
