from spm._runtime import Runtime


def bf_output_image_cfGLM(*args, **kwargs):
    r"""
      Compute phase-amplitude coupling using a general linear model  
        currently takes both low frequency phase and amplitude as regressors  
        needs epoched data - uses epochs for statistics  
        writes out images for summary phase-amplitude coupling and  
        amplitude-amplitude coupling, as well as B coefficients per trial  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DAiSS/bf_output_image_cfGLM.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("bf_output_image_cfGLM", *args, **kwargs)
