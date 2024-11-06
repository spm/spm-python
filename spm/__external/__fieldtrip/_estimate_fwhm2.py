from spm.__wrapper__ import Runtime


def _estimate_fwhm2(*args, **kwargs):
    """
      ESTIMATE_FWHM2(SOURCE, MAXDIST)  
         
        This function computes the Gaussian fwhm of the spatial filters, according to  
        least-squares Gaussian fit including data points up until MAXDIST from the  
        locations of interest.  
          
        This function can only deal with scalar filters.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/estimate_fwhm2.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("estimate_fwhm2", *args, **kwargs)
