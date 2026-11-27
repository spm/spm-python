from spm._runtime import Runtime


def spm_fx_adem_salience(*args, **kwargs):
    r"""
      returns the flow for oculomotor search  
        FORMAT [f]= spm_fx_adem_salience(x,v,a,P)  
         
        x    - hidden states:  
          x(1) - oculomotor angle  
          x(2) - oculomotor angle  
         
        v    - hidden cause  
        P    - parameters  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_fx_adem_salience.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_fx_adem_salience", *args, **kwargs)
