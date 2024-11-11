from spm.__wrapper__ import Runtime


def spm_fx_adem_salience(*args, **kwargs):
    """
      returns the flow for oculomotor search  
        FORMAT [f]= spm_fx_adem_salience(x,v,a,P)  
         
        x    - hidden states:  
          x(1) - oculomotor angle  
          x(2) - oculomotor angle  
         
        v    - hidden cause  
        P    - parameters  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_fx_adem_salience.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_fx_adem_salience", *args, **kwargs)
