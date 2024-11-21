from spm.__wrapper__ import Runtime


def spm_mc_fxa_5(*args, **kwargs):
    """
      equations of motion for the mountain car problem  
        problem  
        FORMAT [f] = spm_mc_fxa_4(x,v,a,P)  
         
        x   - hidden states  
        v   - exogenous inputs  
        a   - action  
        P   - parameters for mountain car  
         
        returns f = dx/dt   
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_mc_fxa_5.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mc_fxa_5", *args, **kwargs)
