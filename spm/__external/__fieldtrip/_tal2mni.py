from spm.__wrap__ import _Runtime


def _tal2mni(*args, **kwargs):
  """  Converts coordinates to MNI brain best guess  
    from Talairach coordinates  
    FORMAT outpoints = tal2mni(inpoints)  
    Where inpoints is N by 3 or 3 by N matrix of coordinates  
     (N being the number of points)  
    outpoints is the coordinate matrix with MNI points  
    Matthew Brett 2/2/01  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/tal2mni.m)
  """

  return _Runtime.call("tal2mni", *args, **kwargs)
