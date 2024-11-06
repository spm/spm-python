from spm.__wrapper__ import Runtime


def spm_fx_adem_write(*args, **kwargs):
    """
      returns the flow for a two-joint arm (with action)  
        FORMAT [f]= spm_fx_adem_reach(x,v,a,P)  
         
        x    - hidden states  
          x(1) - joint angle  
          x(2) - joint angle  
          x(3) - angular velocity  
          x(4) - angular velocity  
        v    - exogenous forces (x,y)  
        a    - action (forces) (x,y)  
        P    - parameters  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_fx_adem_write.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_fx_adem_write", *args, **kwargs)
