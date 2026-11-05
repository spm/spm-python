from spm._runtime import Runtime


def spm_mc_loss_G(*args, **kwargs):
    r"""
      assumed potential gradient for the mountain car problem  
        problem  
        FORMAT [G] = spm_mc_loss_G(x,P)  
         
        x     - hidden states  
        v     - exogenous inputs  
        P.x,k - parameters for gradient function:     G(x(1),P.p)  
        P.q,q - parameters for cost or loss-function: C(x(1),P.q)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_mc_loss_G.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mc_loss_G", *args, **kwargs)
