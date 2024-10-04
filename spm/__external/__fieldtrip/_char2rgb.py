from spm.__wrap__ import _Runtime


def _char2rgb(*args, **kwargs):
  """  CHAR2RGB converts the line color character into the corresponding RGB triplet  
     
    see https://nl.mathworks.com/help/matlab/ref/colorspec.html  
    and https://nl.mathworks.com/matlabcentral/fileexchange/48155-convert-between-rgb-and-color-names  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/char2rgb.m)
  """

  return _Runtime.call("char2rgb", *args, **kwargs)
