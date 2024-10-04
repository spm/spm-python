from spm.__wrap__ import _Runtime


def fiff_write_int_matrix(*args, **kwargs):
  """   
    fiff_write_int_matrix(fid,kind,mat)  
      
    Writes a integer matrix tag  
     
        fid           An open fif file descriptor  
        kind          The tag kind  
        mat           The data matrix  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/fiff_write_int_matrix.m)
  """

  return _Runtime.call("fiff_write_int_matrix", *args, **kwargs, nargout=0)
