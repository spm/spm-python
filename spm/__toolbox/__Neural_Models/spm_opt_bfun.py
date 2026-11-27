from spm._runtime import Runtime


def spm_opt_bfun(*args, **kwargs):
    r"""
       
        FORMAT spm_opt_bfun  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/Neural_Models/spm_opt_bfun.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_opt_bfun", *args, **kwargs, nargout=0)
