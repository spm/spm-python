from spm._runtime import Runtime


def spm_fx_dem_salience(*args, **kwargs):
    r"""
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
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_fx_dem_salience.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_fx_dem_salience", *args, **kwargs)
