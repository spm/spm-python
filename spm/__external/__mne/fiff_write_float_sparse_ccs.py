from spm.__wrap__ import _Runtime


def fiff_write_float_sparse_ccs(*args, **kwargs):
  """   
    fiff_write_float_sparsce_ccs(fid,kind,mat)  
      
    Writes a single-precision sparse (ccs) floating-point matrix tag  
     
        fid           An open fif file descriptor  
        kind          The tag kind  
        mat           The data matrix  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/fiff_write_float_sparse_ccs.m)
  """

  return _Runtime.call("fiff_write_float_sparse_ccs", *args, **kwargs, nargout=0)
