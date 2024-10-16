from spm.__wrapper__ import Runtime


def _threadblocks(*args, **kwargs):
  """  Set the size of a block of threads and grid on a CUDA kernel  
    FORMAT kernel = threadblocks(kernel,d)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/Spatial/private/threadblocks.m)
  """

  return Runtime.call("threadblocks", *args, **kwargs)
