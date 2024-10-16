from spm.__wrapper__ import Runtime


def _mni2tal(*args, **kwargs):
  """  Converts coordinates from MNI brain to best guess  
    for equivalent Talairach coordinates  
    FORMAT outpoints = mni2tal(inpoints)  
    Where inpoints is N by 3 or 3 by N matrix of coordinates  
     (N being the number of points)  
    outpoints is the coordinate matrix with Talairach points  
    Matthew Brett 10/8/99  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/mni2tal.m)
  """

  return Runtime.call("mni2tal", *args, **kwargs)
