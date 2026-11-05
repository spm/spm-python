from spm._runtime import Runtime


def spm_mvb_R2(*args, **kwargs):
    r"""
      Return the proportion of variance explained by the (MVB) MAP estimates  
        FORMAT [R2,X,P] = spm_mvb_R2(MVB)  
         
        MVB - MVB structure  
        R2  - proportion of variance explained  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_mvb_R2.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mvb_R2", *args, **kwargs)
