from spm.__wrapper__ import Runtime


def _getthreads(*args, **kwargs):
  """  Size of block of threads on a CUDA kernel  
    FORMAT s = getthreads(kernel,d)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/Spatial/private/getthreads.m)
  """

  return Runtime.call("getthreads", *args, **kwargs)
