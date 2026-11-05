from spm._runtime import Runtime


def optim_compat(*args, **kwargs):
    r"""
      Compatibility function for optimN and optimNn  
        FORMAT varargout = optim_compat(bc,varargin)  
        bc - boundary condition (0=circulant, 1-Neumann)  
         
        Call the new spm_field function via the old API of the optimN and  
        optimNn functions.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DARTEL/optim_compat.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("optim_compat", *args, **kwargs)
