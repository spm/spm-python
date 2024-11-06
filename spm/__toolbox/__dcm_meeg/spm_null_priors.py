from spm.__wrapper__ import Runtime


def spm_null_priors(*args, **kwargs):
    """
      Prior moments for null (Jacobian) model  
        FORMAT [pE,pC] = spm_null_priors(A,B,C)  
         
        A{1},B{m},C  - binary constraints on extrinsic connections  
         
        pE - prior expectation  
        pC - prior covariance  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_null_priors.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_null_priors", *args, **kwargs)
