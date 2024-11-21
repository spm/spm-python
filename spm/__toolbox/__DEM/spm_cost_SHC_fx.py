from spm.__wrapper__ import Runtime


def spm_cost_SHC_fx(*args, **kwargs):
    """
      equations of motion for foraging problem using SHCs  
        problem  
        FORMAT [f] = spm_cost_SHC_fx(x,v,P)  
         
        x   - hidden states (x.x, x.v x.q and x.a)  
        v   - exogenous inputs  
        P   - parameters  
         
        The parameters associate increases in some physiological states x.q with   
        positions in physical space, encoded by radial basis functions x.a  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_cost_SHC_fx.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_cost_SHC_fx", *args, **kwargs)
