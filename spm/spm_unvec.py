from spm._runtime import Runtime


def spm_unvec(*args, **kwargs):
    r"""
      Unvectorise a vectorised array - a compiled routine  
        FORMAT [varargout] = spm_unvec(vX,varargin)  
        varargin  - numeric, cell or structure array  
        vX        - spm_vec(X)  
         
        i.e. X           = spm_unvec(spm_vec(X),X)  
             [X1,X2,...] = spm_unvec(spm_vec(X1,X2,...),X1,X2,...)  
         
        See spm_vec  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_unvec.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_unvec", *args, **kwargs)
