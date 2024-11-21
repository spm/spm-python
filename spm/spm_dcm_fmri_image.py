from spm.__wrapper__ import Runtime


def spm_dcm_fmri_image(*args, **kwargs):
    """
      Image display of A, B, C and D coupling matrices  
        FORMAT spm_dcm_fmri_image(P)  
         
        P.A, P.B{1}, ...     - connections of weighted directed graph  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dcm_fmri_image.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_fmri_image", *args, **kwargs, nargout=0)
