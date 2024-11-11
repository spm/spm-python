from spm.__wrapper__ import Runtime


def spm_cost_fx(*args, **kwargs):
    """
      equations of motion for foragaing problem  
        problem  
        FORMAT [f] = spm_cost_fx(x,v,P)  
         
        x   - hidden states  
        v   - exogenous inputs  
        P.p - parameters for gradient function:     G(x(1),P.p)  
         
        returns f = dx/dt = f  = [x(2);  
                                  G - x(2)*C]*dt;  
         
        where C determines divergence of flow x(2) at any position x(1).  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_cost_fx.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_cost_fx", *args, **kwargs)
