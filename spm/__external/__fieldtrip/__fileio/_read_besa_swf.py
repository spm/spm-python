from spm.__wrap__ import _Runtime


def _read_besa_swf(*args, **kwargs):
  """  READ_BESA_SWF  
     
    Use as  
      [swf] = read_besa_swf(filename)  
     
    This will return a structure with the header information in  
      swf.label     cell-array with labels  
      swf.data      data matrix, Nchan X Npnts  
      swf.npnt  
      swf.tsb  
      swf.di  
      swf.sb  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_besa_swf.m)
  """

  return _Runtime.call("read_besa_swf", *args, **kwargs)
