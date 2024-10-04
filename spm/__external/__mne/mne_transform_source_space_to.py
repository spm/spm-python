from spm.__wrap__ import _Runtime


def mne_transform_source_space_to(*args, **kwargs):
  """   
    [res] = mne_transform_source_space_to(src,dest,trans)  
     
    Transform source space data to the desired coordinate system  
     
    src        - The source space to transform  
    dest       - The id of the destination coordinate system (FIFFV_COORD_...)  
    trans      - The coordinate transformation structure to use  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/mne_transform_source_space_to.m)
  """

  return _Runtime.call("mne_transform_source_space_to", *args, **kwargs)
