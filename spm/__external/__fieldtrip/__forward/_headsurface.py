from spm.__wrap__ import _Runtime


def _headsurface(*args, **kwargs):
  """  HEADSURFACE constructs a triangulated description of the skin or brain  
    surface from a volume conduction model, from a set of electrodes or  
    gradiometers, or from a combination of the two. It returns a closed  
    surface.  
     
    Use as  
      [pos, tri] = headsurface(headmodel, sens, ...)  
    where  
      headmodel      = volume conduction model (structure)  
      sens           = electrode or gradiometer array (structure)  
     
    Optional arguments should be specified in key-value pairs:  
      surface        = 'skin' or 'brain' (default = 'skin')  
      npos           = number of vertices (default is determined automatic)  
      downwardshift  = boolean, this will shift the lower rim of the helmet down with approximately 1/4th of its radius (default is 1)  
      inwardshift    = number (default = 0)  
      headshape      = string, file containing the head shape  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/forward/private/headsurface.m)
  """

  return _Runtime.call("headsurface", *args, **kwargs)
