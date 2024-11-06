from spm.__wrapper__ import Runtime


def glm_phi(*args, **kwargs):
    """
      Estimate connectivity parameters using GLM/EMA method  
        FORMAT [A,fint] = glm_phi(phi,dt,fb)  
         
        phi    -  [N x Nr] matrix of phase time series  
               -  (N time points, Nr regions)  
        dt     -  sample period  
        fb     -  bandwidth parameter  
         
        A      -  [Nr x Nr] normalised connectivities  
        fint   -  [Nr x 1] intrinsic frequencies  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/man/example_scripts/glm_phi.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("glm_phi", *args, **kwargs)
