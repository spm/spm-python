from spm._runtime import Runtime


def spm_vol_nifti(*args, **kwargs):
    r"""
      Get header information for a NIFTI-1 image  
        FORMAT V = spm_vol_nifti(P,n)  
        P   - filename or NIfTI object  
        n   - volume id (a 1x2 array, e.g. [3,1])  
         
        V   - a structure containing the image volume information  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_vol_nifti.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_vol_nifti", *args, **kwargs)
