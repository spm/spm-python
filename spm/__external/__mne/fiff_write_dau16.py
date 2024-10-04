from spm.__wrap__ import _Runtime


def fiff_write_dau16(*args, **kwargs):
  """   
    fiff_write_dau16(fid, kind, data)  
     
    Writes a 16-bit integer tag to a fif file  
     
        fid           An open fif file descriptor  
        kind          Tag kind  
        data          The integers to use as data  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/fiff_write_dau16.m)
  """

  return _Runtime.call("fiff_write_dau16", *args, **kwargs, nargout=0)
