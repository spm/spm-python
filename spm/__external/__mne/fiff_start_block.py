from spm.__wrapper__ import Runtime


def fiff_start_block(*args, **kwargs):
  """   
    fiff_start_block(fid,kind)  
      
    Writes a FIFF_BLOCK_START tag  
     
        fid           An open fif file descriptor  
        kind          The block kind to start  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/fiff_start_block.m)
  """

  return Runtime.call("fiff_start_block", *args, **kwargs, nargout=0)
