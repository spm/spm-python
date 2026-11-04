from spm._runtime import Runtime


def spm_mvb_cvk_display(*args, **kwargs):
    r"""
      Model display for MVB with cross-validation  
        FORMAT spm_mvb_cvk_display(MVB)  
        MVB  - multivariate Bayes structure, select one if not provided  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_mvb_cvk_display.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mvb_cvk_display", *args, **kwargs, nargout=0)
