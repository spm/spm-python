from spm.__wrap__ import _Runtime


def spm_spectral_plot(*args, **kwargs):
  """  subplot for spectral arrays  
    FORMAT spm_spectral_plot(Hz,csd,str,xlab,ylab)  
     
    str  - format (default: '-')  
    xlab - xlabel (default: 'Hz')  
    ylab - ylabel (default: 'power')  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/spectral/spm_spectral_plot.m)
  """

  return _Runtime.call("spm_spectral_plot", *args, **kwargs, nargout=0)
