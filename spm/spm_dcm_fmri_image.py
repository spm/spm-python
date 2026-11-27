from spm._runtime import Runtime


def spm_dcm_fmri_image(*args, **kwargs):
    r"""
      Image display of A, B, C and D coupling matrices  
        FORMAT spm_dcm_fmri_image(P)  
         
        P.A, P.B{1}, ...     - connections of weighted directed graph  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_dcm_fmri_image.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_dcm_fmri_image", *args, **kwargs, nargout=0)
