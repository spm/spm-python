from spm.__wrap__ import _Runtime


def fiff_write_ctf_comp(*args, **kwargs):
  """   
    fiff_write_ctf_comp(fid,comps,ch_rename)  
     
    Writes the CTF compensation data into a fif file  
     
        fid           An open fif file descriptor  
        comps         The compensation data to write  
        ch_rename     Short-to-long channel name mapping  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/fiff_write_ctf_comp.m)
  """

  return _Runtime.call("fiff_write_ctf_comp", *args, **kwargs, nargout=0)
