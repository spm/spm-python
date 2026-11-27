from spm._runtime import Runtime


def spm_cost_fxa(*args, **kwargs):
    r"""
      equations of motion for a foraging problem  
        problem  
        FORMAT [f] = spm_cost_fxa(x,v,a,P)  
         
        x   - hidden states  
        v   - exogenous inputs  
        a   - action  
        P   - parameters for mountain car  
         
        returns f = dx/dt   
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_cost_fxa.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_cost_fxa", *args, **kwargs)
