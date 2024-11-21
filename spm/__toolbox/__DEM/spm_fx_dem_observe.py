from spm.__wrapper__ import Runtime


def spm_fx_dem_observe(*args, **kwargs):
    """
      returns the flow for a two-joint arm (writing with SHC)  
        FORMAT [f]= spm_fx_dem_observe(x,v,P)  
         
          x.x(1) - joint angle  
          x.x(2) - joint angle  
          x.x(3) - angular velocity  
          x.x(4) - angular velocity  
         
          x.a(1) - attraction (location 1)  
          x.a(2) - attraction (location 2)  
          x.a(3) - attraction (location 3)  
           ...  
         
        v    - hidden states  
          v(1) - not used  
        P    - parameters (locations of point attratcors in state-space)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_fx_dem_observe.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_fx_dem_observe", *args, **kwargs)
