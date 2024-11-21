from spm.__wrapper__ import Runtime


def spm_cost_SHC_fxa(*args, **kwargs):
    """
      equations of motion for a foraging problem  
        FORMAT [f] = spm_cost_SHC_fxa(x,v,a,P)  
         
        x   - hidden states  
        v   - exogenous inputs  
        a   - action  
        P   - parameters for mountain car  
         
        returns f = dx/dt (see spm_cost_SHC_fx)  
        These equations of motion model dissipative flow x.x and x.v on a flat   
        potential and increases in physiological states x.q as radial basis   
        functions of secrete locations. The agent has to discover these   
        locations % using an appropriate policy. This generative process would   
        also substitute for Morris water-maze simulations or unbounded saccades.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_cost_SHC_fxa.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_cost_SHC_fxa", *args, **kwargs)
