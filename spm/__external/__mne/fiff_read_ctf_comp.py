from spm.__wrap__ import _Runtime


def fiff_read_ctf_comp(*args, **kwargs):
  """   
    [ compdata ] = fiff_read_ctf_comp(fid,node,chs,ch_rename)  
     
    Read the CTF software compensation data from the given node  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/fiff_read_ctf_comp.m)
  """

  return _Runtime.call("fiff_read_ctf_comp", *args, **kwargs)
