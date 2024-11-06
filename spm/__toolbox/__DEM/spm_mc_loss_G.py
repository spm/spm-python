from spm.__wrapper__ import Runtime


def spm_mc_loss_G(*args, **kwargs):
    """
      assumed potential gradient for the mountain car problem  
        problem  
        FORMAT [G] = spm_mc_loss_G(x,P)  
         
        x     - hidden states  
        v     - exogenous inputs  
        P.x,k - parameters for gradient function:     G(x(1),P.p)  
        P.q,q - parameters for cost or loss-function: C(x(1),P.q)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_mc_loss_G.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mc_loss_G", *args, **kwargs)
