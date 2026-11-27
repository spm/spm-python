from spm._runtime import Runtime


def spm_dcm_peb_review(*args, **kwargs):
    r"""
      Review tool for DCM PEB models  
        FORMAT spm_dcm_peb_review(PEB,DCM)  
         
        PEB - PEB model to review  
        DCM - (Optional) A single DCM or cell array of DCMs. Data is used to   
              enhance the GUI.  
         
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_dcm_peb_review.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_dcm_peb_review", *args, **kwargs, nargout=0)
