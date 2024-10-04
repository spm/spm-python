from spm.__wrap__ import _Runtime


def fiff_write_coord_trans(*args, **kwargs):
  """   
    fiff_write_coord_trans(fid,trans)  
      
    Writes a coordinate transformation structure  
     
        fid           An open fif file descriptor  
        trans         The coordinate transfomation structure  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/fiff_write_coord_trans.m)
  """

  return _Runtime.call("fiff_write_coord_trans", *args, **kwargs, nargout=0)
