from spm.__wrap__ import _Runtime


def _threadblocks(*args, **kwargs):
  """  Set the size of a block of threads and grid on a CUDA kernel  
    FORMAT kernel = threadblocks(kernel,d)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/Spatial/private/threadblocks.m)
  """

  return _Runtime.call("threadblocks", *args, **kwargs)
