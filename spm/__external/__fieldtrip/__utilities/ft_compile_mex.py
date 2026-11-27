from spm._runtime import Runtime


def ft_compile_mex(*args, **kwargs):
    r"""
      FT_COMPILE_MEX is deprecated, use src/Makefile instead  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/utilities/ft_compile_mex.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_compile_mex", *args, **kwargs, nargout=0)
