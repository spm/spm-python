from spm.__wrap__ import _Runtime


def fiff_write_int(*args, **kwargs):
  """   
    fiff_write_int(fid,kind,data)  
      
    Writes a 32-bit integer tag to a fif file  
     
        fid           An open fif file descriptor  
        kind          Tag kind  
        data          The integers to use as data  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/fiff_write_int.m)
  """

  return _Runtime.call("fiff_write_int", *args, **kwargs, nargout=0)
