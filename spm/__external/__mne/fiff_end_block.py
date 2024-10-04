from spm.__wrap__ import _Runtime


def fiff_end_block(*args, **kwargs):
  """   
    fiff_end_block(fid, kind)  
     
    Writes a FIFF_BLOCK_END tag  
     
        fid           An open fif file descriptor  
        kind          The block kind to end  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/fiff_end_block.m)
  """

  return _Runtime.call("fiff_end_block", *args, **kwargs, nargout=0)
