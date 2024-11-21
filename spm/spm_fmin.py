from spm.__wrapper__ import Runtime


def spm_fmin(*args, **kwargs):
    """
      Objective function minimisation  
        FORMAT [P,F] = spm_fmin('fun',P,C,varargin)  
         
        fun - function or inline function f - fun(P,varargin)  
        P   - free parameters (prior mean)  
        C   - prior covariance  
         
        P   - optimised parameters  
        f   - optimised value of fun(P)  
         
       --------------------------------------------------------------------------  
        spm_fmin is a slow but robust function minimiser that uses a stochastic  
        sampling of the objective function to be minimised (supplemented by a  
        line search along the principal eigenvariate at the current sampling  
        density. The sampling density is approximated with a Gaussian (first and  
        second order moments) using that the sampling density is:  
         
                  p(P) = (1/Z)*exp(-fun(P)/T)  
         
        where the temperature; T is the sample standard deviation of the sampled  
        objective function.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_fmin.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_fmin", *args, **kwargs)
