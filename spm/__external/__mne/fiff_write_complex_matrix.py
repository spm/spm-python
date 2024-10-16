from spm.__wrapper__ import Runtime


def fiff_write_complex_matrix(*args, **kwargs):
  """   
    fiff_write_complex_matrix(fid,kind,mat)  
     
    Writes a single-precision complex matrix tag  
     
        fid           An open fif file descriptor  
        kind          The tag kind  
        mat           The data matrix  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/fiff_write_complex_matrix.m)
  """

  return Runtime.call("fiff_write_complex_matrix", *args, **kwargs, nargout=0)
