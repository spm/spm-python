from spm._runtime import Runtime


def DEM_demo_factor_analysis(*args, **kwargs):
    r"""
      Demo for Probabilistic Factor Analysis; This uses a hierarchical model  
        under the constraint that the causes have a deterministic and stochastic  
        components.  The aim is to recover the true subspace of the real causes.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/DEM_demo_factor_analysis.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("DEM_demo_factor_analysis", *args, **kwargs, nargout=0)
