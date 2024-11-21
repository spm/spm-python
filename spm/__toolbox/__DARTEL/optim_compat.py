from spm.__wrapper__ import Runtime


def optim_compat(*args, **kwargs):
    """
      Compatibility function for optimN and optimNn  
        FORMAT varargout = optim_compat(bc,varargin)  
        bc - boundary condition (0=circulant, 1-Neumann)  
         
        Call the new spm_field function via the old API of the optimN and  
        optimNn functions.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DARTEL/optim_compat.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("optim_compat", *args, **kwargs)
