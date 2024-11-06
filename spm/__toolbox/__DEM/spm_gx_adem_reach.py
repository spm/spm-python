from spm.__wrapper__ import Runtime


def spm_gx_adem_reach(*args, **kwargs):
    """
      returns the prediction for a two-joint arm (with action)  
        FORMAT [g] = spm_gx_adem_reach(x,v,a,P)  
         
        x    - hidden states  
          x(1) - joint angle  
          x(2) - joint angle  
          x(3) - angular velocity  
          x(4) - angular velocity  
        v    - causal states  
          v(1) - target location (x)  
          v(2) - target location (y)  
          v(3) - force (cue strength)  
        P    - parameters  
        a    - action  
        P    - parameters  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_gx_adem_reach.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_gx_adem_reach", *args, **kwargs)
