from spm.__wrap__ import _Runtime


def _getthreads(*args, **kwargs):
  """  Size of block of threads on a CUDA kernel  
    FORMAT s = getthreads(kernel,d)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/Spatial/private/getthreads.m)
  """

  return _Runtime.call("getthreads", *args, **kwargs)
