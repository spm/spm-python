from spm.__wrapper__ import Runtime


def spm_gx_adem_write(*args, **kwargs):
    """
      returns the prediction for a two-joint arm (proprioception and vision)  
        FORMAT [g]= spm_gx_adem_write(x,v,a,P)  
         
        x    - hidden states:  
          x(1) - joint angle  
          x(2) - joint angle  
          x(3) - angular velocity  
          x(4) - angular velocity  
        v    - causal states{  
          v(1) - exogenous force (x)  
          v(2) - exogenous force (y)  
        a    - action  
        P    - parameters  
         
        g    - sensations:  
          g(1) - joint angle (proprioception)  
          g(2) - joint angle (proprioception)  
          g(3) - arm location (visual)  
          g(4) - arm location (visual)  
          
        As for spm_dem_reach but with no visual target  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_gx_adem_write.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_gx_adem_write", *args, **kwargs)
