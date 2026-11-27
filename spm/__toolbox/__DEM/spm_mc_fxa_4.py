from spm._runtime import Runtime


def spm_mc_fxa_4(*args, **kwargs):
    r"""
      equations of motion for the mountain car problem  
        problem  
        FORMAT [f] = spm_mc_fxa_4(x,v,a,P)  
         
        x   - hidden states  
        v   - exogenous inputs  
        a   - action  
        P   - parameters for mountain car  
         
        returns f = dx/dt   
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_mc_fxa_4.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mc_fxa_4", *args, **kwargs)
