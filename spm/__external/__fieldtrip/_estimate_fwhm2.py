from spm._runtime import Runtime


def _estimate_fwhm2(*args, **kwargs):
    r"""
      ESTIMATE_FWHM2(SOURCE, MAXDIST)  
         
        This function computes the Gaussian fwhm of the spatial filters, according to  
        least-squares Gaussian fit including data points up until MAXDIST from the  
        locations of interest.  
          
        This function can only deal with scalar filters.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/estimate_fwhm2.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("estimate_fwhm2", *args, **kwargs)
