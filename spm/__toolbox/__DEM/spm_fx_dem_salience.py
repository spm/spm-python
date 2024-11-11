from spm.__wrapper__ import Runtime


def spm_fx_dem_salience(*args, **kwargs):
    """
      returns the flow for visual search  
        FORMAT [f]= spm_fx_dem_salience(x,v,P)  
         
        x    - hidden states:  
          o(1) - oculomotor angle  
          o(2) - oculomotor angle  
          x(1) - relative amplitude of visual hypothesis 1  
          x(2) - relative amplitude of visual hypothesis 2  
          x(3) - ...  
         
        v    - hidden causes - attracting location  
        P    - parameters  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_fx_dem_salience.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_fx_dem_salience", *args, **kwargs)
