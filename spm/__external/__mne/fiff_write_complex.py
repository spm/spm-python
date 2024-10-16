from spm.__wrapper__ import Runtime


def fiff_write_complex(*args, **kwargs):
  """   
    fiff_write_complex(fid,kind,data)  
      
    Writes a single-precision complex tag to a fif file  
     
        fid           An open fif file descriptor  
        kind          Tag kind  
        data          The data  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/fiff_write_complex.m)
  """

  return Runtime.call("fiff_write_complex", *args, **kwargs, nargout=0)
