from spm.__wrapper__ import Runtime


def strel_bol(*args, **kwargs):
  """  STREL_BOL constructs a 3D sphere with the specified radius  
    that can be used as structural element in 3D image processing  
     
    See STREL, IMERODE, IMDILATE (image processing toolbox)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/strel_bol.m)
  """

  return Runtime.call("strel_bol", *args, **kwargs)
