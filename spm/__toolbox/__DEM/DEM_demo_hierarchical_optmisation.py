from spm._runtime import Runtime


def DEM_demo_hierarchical_optmisation(*args, **kwargs):
    r"""
      This is the same as spm_nlsi_GH but tries to model the free energy as a  
        function of conditional expectations using a sparse mixture of scaled  
        Gaussians. The objective is to account for local maxima when optimising  
        free energy by recasting the problem in terms of a parameterised mapping   
        from conditional expectation to free energy explicitly.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/DEM_demo_hierarchical_optmisation.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("DEM_demo_hierarchical_optmisation", *args, **kwargs, nargout=0)
