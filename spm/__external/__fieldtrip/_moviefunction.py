from spm.__wrapper__ import Runtime


def _moviefunction(*args, **kwargs):
  """  we need cfg.plotfun to plot the data  
    data needs to be 3D, N x time x freq (last can be singleton)  
      N needs to correspond to number of vertices (channels, gridpoints, etc)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/moviefunction.m)
  """

  return Runtime.call("moviefunction", *args, **kwargs, nargout=0)
