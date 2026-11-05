from spm._runtime import Runtime


def spm_fx_adem_write(*args, **kwargs):
    r"""
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
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_fx_adem_write.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_fx_adem_write", *args, **kwargs)
