from spm._runtime import Runtime


def spm_mvb_cvk_display(*args, **kwargs):
    """
      Model display for MVB with cross-validation  
        FORMAT spm_mvb_cvk_display(MVB)  
        MVB  - multivariate Bayes structure, select one if not provided  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_mvb_cvk_display.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mvb_cvk_display", *args, **kwargs, nargout=0)
