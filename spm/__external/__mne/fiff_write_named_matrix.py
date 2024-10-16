from spm.__wrapper__ import Runtime


def fiff_write_named_matrix(*args, **kwargs):
  """   
    fiff_write_named_matrix(fid,kind,mat)  
      
    Writes a named single-precision floating-point matrix  
     
        fid           An open fif file descriptor  
        kind          The tag kind to use for the data  
        mat           The data matrix  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/fiff_write_named_matrix.m)
  """

  return Runtime.call("fiff_write_named_matrix", *args, **kwargs, nargout=0)
