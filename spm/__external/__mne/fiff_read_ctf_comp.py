from spm.__wrapper__ import Runtime


def fiff_read_ctf_comp(*args, **kwargs):
  """   
    [ compdata ] = fiff_read_ctf_comp(fid,node,chs,ch_rename)  
     
    Read the CTF software compensation data from the given node  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/fiff_read_ctf_comp.m)
  """

  return Runtime.call("fiff_read_ctf_comp", *args, **kwargs)
