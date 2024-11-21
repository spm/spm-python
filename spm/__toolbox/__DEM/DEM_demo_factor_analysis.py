from spm.__wrapper__ import Runtime


def DEM_demo_factor_analysis(*args, **kwargs):
    """
      Demo for Probabilistic Factor Analysis; This uses a hierarchical model  
        under the constraint that the causes have a deterministic and stochastic  
        components.  The aim is to recover the true subspace of the real causes.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_demo_factor_analysis.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_demo_factor_analysis", *args, **kwargs, nargout=0)
