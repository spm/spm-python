from spm.__wrap__ import _Runtime


def spm_opm_plotScalpData(*args, **kwargs):
  """  Display M/EEG interpolated sensor data on a scalp image  
    FORMAT D = spm_opm_amm(S)  
      S               - input structure  
     fields of S:  
      S.D             - SPM MEEG object                                - Default: no Default  
      S.T             - time point to initalise to                    - Default: first sample    
      S.display       - string to deermine what is plotted   -Default: 'RADIAL'  
    OUTPUT:  
      f          - the handle of the figure which displays the interpolated  
                   data  
   __________________________________________________________________________  
     
    This function creates a figure whose purpose is to display an  
    interpolation of the sensor data on the scalp (as an image).  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/MEEGtools/spm_opm_plotScalpData.m)
  """

  return _Runtime.call("spm_opm_plotScalpData", *args, **kwargs)
