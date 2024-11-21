from spm.__wrapper__ import Runtime


def spm_gn_fmin(*args, **kwargs):
    """
      Objective function minimisation using Gauss-Newton line searches  
        FORMAT [P,F] = spm_gn_fmin(fun,Q,C,varargin)  
         
        fun - function or inline function f - fun(P,varargin)  
        P   - free parameters (prior mean)  
        C   - prior covariance  
         
        P   - optimised parameters  
        f   - optimised value of fun(P)  
         
       --------------------------------------------------------------------------  
        spm_fmin is a slow but robust function minimiser that uses a Gauss-Newton  
        method and successive line searches.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_gn_fmin.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_gn_fmin", *args, **kwargs)
