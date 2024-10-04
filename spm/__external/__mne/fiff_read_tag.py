from spm.__wrap__ import _Runtime


def fiff_read_tag(*args, **kwargs):
  """   
    [tag] = fiff_read_tag(fid,pos)  
     
    Read one tag from a fif file.  
    if pos is not provided, reading starts from the current file position  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/fiff_read_tag.m)
  """

  return _Runtime.call("fiff_read_tag", *args, **kwargs)
