from spm.__wrap__ import _Runtime


def _read_besa_src(*args, **kwargs):
  """  READ_BESA_SRC reads a beamformer source reconstruction from a BESA file  
     
    Use as  
      [src] = read_besa_src(filename)  
     
    The output structure contains a minimal representation of the contents  
    of the file.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/read_besa_src.m)
  """

  return _Runtime.call("read_besa_src", *args, **kwargs)
