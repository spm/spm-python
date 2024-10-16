from spm.__wrapper__ import Runtime


def spm_smoothto8bit(*args, **kwargs):
  """  3 dimensional convolution of an image to 8bit data in memory  
    FORMAT VO = spm_smoothto8bit(V,fwhm)  
    V     - mapped image to be smoothed  
    fwhm  - FWHM of Gaussian filter width in mm  
    VO    - smoothed volume in a form that can be used by the  
            spm_*_vol.mex* functions.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_smoothto8bit.m)
  """

  return Runtime.call("spm_smoothto8bit", *args, **kwargs)
