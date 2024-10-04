from spm.__wrap__ import _Runtime


def fiff_invert_transform(*args, **kwargs):
  """   
    [itrans] = fiff_invert_transform(trans)  
     
    Invert a coordinate transformation  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/fiff_invert_transform.m)
  """

  return _Runtime.call("fiff_invert_transform", *args, **kwargs)
