from spm._runtime import Runtime


def spm_argmax(*args, **kwargs):
    r"""
      Function minimisation using Gauss-Newton  
        FORMAT [P,f] = spm_argmax('fun',varargin,i)  
         
        fun      - inline function f - fun(P,varargin)  
        varargin - function arguments  
        i        - argument to minimise: varargin{i}  
         
        P   - optimised argument  
        f   - optimised value of fun(P)  
         
       --------------------------------------------------------------------------  
        spm_argmax uses numerical derivatives and a and adaptive Gauss-Newton   
        scheme: see also spm_argmin.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_argmax.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_argmax", *args, **kwargs)
