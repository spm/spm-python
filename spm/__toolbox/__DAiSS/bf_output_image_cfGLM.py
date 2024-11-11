from spm.__wrapper__ import Runtime


def bf_output_image_cfGLM(*args, **kwargs):
    """
      Compute phase-amplitude coupling using a general linear model  
        currently takes both low frequency phase and amplitude as regressors  
        needs epoched data - uses epochs for statistics  
        writes out images for summary phase-amplitude coupling and  
        amplitude-amplitude coupling, as well as B coefficients per trial  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_output_image_cfGLM.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("bf_output_image_cfGLM", *args, **kwargs)
