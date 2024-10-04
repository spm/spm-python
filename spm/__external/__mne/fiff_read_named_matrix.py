from spm.__wrap__ import _Runtime


def fiff_read_named_matrix(*args, **kwargs):
  """   
    [mat] = fiff_read_named_matrix(fid,node)  
     
    Read named matrix from the given node  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/fiff_read_named_matrix.m)
  """

  return _Runtime.call("fiff_read_named_matrix", *args, **kwargs)
