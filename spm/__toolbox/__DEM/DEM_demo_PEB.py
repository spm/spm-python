from spm.__wrapper__ import Runtime


def DEM_demo_PEB(*args, **kwargs):
    """
      DEM demo for a hierarchical linear model (MFX).  This inversion is  
        cross-validated with restricted maximum likelihood using and parametric  
        empirical Bayes (spm_PEB). It uses a simple two level model that embodies  
        empirical shrinkage priors on the first-level parameters (c.f.,  
        DEM_demo_GLM, with no empirical priors)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_demo_PEB.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_demo_PEB", *args, **kwargs, nargout=0)
