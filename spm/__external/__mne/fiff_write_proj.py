from spm.__wrap__ import _Runtime


def fiff_write_proj(*args, **kwargs):
  """   
    fiff_write_proj(fid,projs,ch_rename)  
     
    Writes the projection data into a fif file  
     
        fid           An open fif file descriptor  
        projs         The compensation data to write  
        ch_rename     Short-to-long channel name mapping  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/fiff_write_proj.m)
  """

  return _Runtime.call("fiff_write_proj", *args, **kwargs, nargout=0)
