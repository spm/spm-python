from spm._runtime import Runtime


def spm_dcm_review(*args, **kwargs):
    r"""
      Review an estimated DCM  
        FORMAT spm_dcm_review(DCM,action)  
         
        DCM    - DCM structure or its filename  
        action - one of:  
                 'fixed connections'  
                 ['    effects of ' DCM.U.name{i}];  
                 'contrast of connections'  
                 'location of regions'  
                 'inputs'  
                 'outputs'  
                 'kernels'  
                 'estimates of states'  
                 'estimates of parameters'  
                 'estimates of precisions'  
                 ['   hidden states: ' DCM.Y.name{i}]  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_dcm_review.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_dcm_review", *args, **kwargs, nargout=0)
