from spm._runtime import Runtime


def _estimate_fwhm1(*args, **kwargs):
    r"""
      ESTIMATE_FWHM1(SOURCE, REMOVECENTER)  
         
        This function computes the fwhm of the spatial filters, according to  
        Barnes et al 2003. the input source-structure should contain the filters  
        The fwhm-volume is appended to the output source-structure. It is assumed  
        that the dipole positions are defined on a regularly spaced 3D grid.  
          
        This function can only deal with scalar filters.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/estimate_fwhm1.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("estimate_fwhm1", *args, **kwargs)
