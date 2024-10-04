from spm.__wrap__ import _Runtime


def fiff_write_id(*args, **kwargs):
  """   
    fiff_write_id(fid,kind,id)  
      
    Writes fiff id   
     
        fid           An open fif file descriptor  
        kind          The tag kind  
        id            The id to write  
     
    If the id argument is missing it will be generated here  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/fiff_write_id.m)
  """

  return _Runtime.call("fiff_write_id", *args, **kwargs, nargout=0)
