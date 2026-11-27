from spm._runtime import Runtime


def DEM_demo_PEB(*args, **kwargs):
    r"""
      DEM demo for a hierarchical linear model (MFX).  This inversion is  
        cross-validated with restricted maximum likelihood using and parametric  
        empirical Bayes (spm_PEB). It uses a simple two level model that embodies  
        empirical shrinkage priors on the first-level parameters (c.f.,  
        DEM_demo_GLM, with no empirical priors)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/DEM_demo_PEB.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("DEM_demo_PEB", *args, **kwargs, nargout=0)
