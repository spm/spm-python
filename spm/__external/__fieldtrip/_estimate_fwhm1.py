from spm.__wrapper__ import Runtime


def _estimate_fwhm1(*args, **kwargs):
    """
      ESTIMATE_FWHM1(SOURCE, REMOVECENTER)  
         
        This function computes the fwhm of the spatial filters, according to  
        Barnes et al 2003. the input source-structure should contain the filters  
        The fwhm-volume is appended to the output source-structure. It is assumed  
        that the dipole positions are defined on a regularly spaced 3D grid.  
          
        This function can only deal with scalar filters.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/estimate_fwhm1.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("estimate_fwhm1", *args, **kwargs)
