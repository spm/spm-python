from spm.__wrap__ import _Runtime


def _estimate_fwhm2(*args, **kwargs):
  """  ESTIMATE_FWHM2(SOURCE, MAXDIST)  
     
    This function computes the Gaussian fwhm of the spatial filters, according to  
    least-squares Gaussian fit including data points up until MAXDIST from the  
    locations of interest.  
      
    This function can only deal with scalar filters.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/estimate_fwhm2.m)
  """

  return _Runtime.call("estimate_fwhm2", *args, **kwargs)
