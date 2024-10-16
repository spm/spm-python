from spm.__wrapper__ import Runtime


def fiff_write_int(*args, **kwargs):
  """   
    fiff_write_int(fid,kind,data)  
      
    Writes a 32-bit integer tag to a fif file  
     
        fid           An open fif file descriptor  
        kind          Tag kind  
        data          The integers to use as data  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/fiff_write_int.m)
  """

  return Runtime.call("fiff_write_int", *args, **kwargs, nargout=0)
