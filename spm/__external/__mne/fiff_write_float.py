from spm.__wrap__ import _Runtime


def fiff_write_float(*args, **kwargs):
  """   
    fiff_write_float(fid,kind,data)  
      
    Writes a single-precision floating point tag to a fif file  
     
        fid           An open fif file descriptor  
        kind          Tag kind  
        data          The data  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/fiff_write_float.m)
  """

  return _Runtime.call("fiff_write_float", *args, **kwargs, nargout=0)
