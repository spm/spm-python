from spm.__wrap__ import _Runtime


def ft_sourcedepth(*args, **kwargs):
  """  FT_SOURCEDEPTH computes the distance from the source to the surface of  
    the source compartment (usually the brain) in the volume conduction model.  
     
    Use as  
      depth = ft_sourcedepth(dippos, headmodel);  
    where  
      dippos    =  Nx3 matrix with the position of N sources  
      headmodel =  structure describing volume condition model  
     
    A negative depth indicates that the source is inside the source  
    compartment, positive indicates outside.  
     
    See also FT_INSIDE_HEADMODEL  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/forward/ft_sourcedepth.m)
  """

  return _Runtime.call("ft_sourcedepth", *args, **kwargs)
