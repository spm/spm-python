from spm.__wrapper__ import Runtime


def spm_fx_adem_pursuit(*args, **kwargs):
    """
      returns the flow for occulomotor pursuit (with action)  
        FORMAT [f]= spm_fx_adem_pursuit(x,v,a,P)  
         
        x    - hidden states:  
          x.o(1) - oculomotor angle  
          x.o(2) - oculomotor angle  
          x.x(1) - target location (visual) - extrinsic coordinates (Cartesian)  
          x.x(2) - target location (visual) - extrinsic coordinates (Cartesian)  
          x.a(:) - attractor (SHC) states  
         
        v    - hidden cause (speed)  
        P    - parameters  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_fx_adem_pursuit.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_fx_adem_pursuit", *args, **kwargs)
