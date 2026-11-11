from spm._runtime import Runtime


def spm_gx_adem_salience(*args, **kwargs):
    r"""
      returns the prediction for visual search (proprioception and vision)  
        FORMAT [g]= spm_gx_adem_salience(x,v,a,P)  
         
        x    - hidden states:  
          o(1) - oculomotor angle  
          o(2) - oculomotor angle  
         
        v    - hidden causes  
        P    - parameters  
         
        g    - sensations:  
          g(1) - oculomotor angle (proprioception - x)  
          g(2) - oculomotor angle (proprioception - y)  
          g(3) - retinal input - channel 1  
          g(4) - retinal input - channel 2  
          g(5) - ...  
          
        As for spm_dem_reach but with no visual target  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_gx_adem_salience.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_gx_adem_salience", *args, **kwargs)
