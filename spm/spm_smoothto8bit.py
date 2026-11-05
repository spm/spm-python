from spm._runtime import Runtime


def spm_smoothto8bit(*args, **kwargs):
    r"""
      3 dimensional convolution of an image to 8bit data in memory  
        FORMAT VO = spm_smoothto8bit(V,fwhm)  
        V     - mapped image to be smoothed  
        fwhm  - FWHM of Gaussian filter width in mm  
        VO    - smoothed volume in a form that can be used by the  
                spm_*_vol.mex* functions.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_smoothto8bit.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_smoothto8bit", *args, **kwargs)
