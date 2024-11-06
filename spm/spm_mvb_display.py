from spm.__wrapper__ import Runtime


def spm_mvb_display(*args, **kwargs):
    """
      Model display for MVB  
        FORMAT spm_mvb_display(MVB)  
        MVB  - multivariate Bayes structure, select one if not provided  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_mvb_display.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mvb_display", *args, **kwargs, nargout=0)
