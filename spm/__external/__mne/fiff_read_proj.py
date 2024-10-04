from spm.__wrap__ import _Runtime


def fiff_read_proj(*args, **kwargs):
  """   
    [ projdata ] = fiff_read_proj(fid,node,ch_rename)  
     
    Read the SSP data under a given directory node  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/fiff_read_proj.m)
  """

  return _Runtime.call("fiff_read_proj", *args, **kwargs)
