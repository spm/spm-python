from spm.__wrap__ import _Runtime


def fiff_end_file(*args, **kwargs):
  """   
    fiff_end_file(fid)  
     
    Writes the closing tags to a fif file and closes the file  
     
        fid           An open fif file descriptor  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/fiff_end_file.m)
  """

  return _Runtime.call("fiff_end_file", *args, **kwargs, nargout=0)
