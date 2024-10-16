from spm.__wrapper__ import Runtime


def _fixinside(*args, **kwargs):
  """  FIXINSIDE ensures that the region of interest (which is indicated by the  
    field "inside") is consistently defined for source structures and volume  
    structures. Furthermore, it solves backward compatibility problems.  
     
    Use as  
      [source] = fixinside(source, 'logical');  
    or  
      [source] = fixinside(source, 'index');  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/fixinside.m)
  """

  return Runtime.call("fixinside", *args, **kwargs)
