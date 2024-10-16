from spm.__wrapper__ import Runtime


def _dist(*args, **kwargs):
  """  DIST computes the euclidian distance between the columns of the input matrix  
     
    Use as  
      [d] = dist(x)  
    where x is for example an 3xN matrix with positions in 3D space.  
     
    This function serves as a replacement for the dist function in the Neural  
    Networks toolbox.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/plotting/private/dist.m)
  """

  return Runtime.call("dist", *args, **kwargs)
