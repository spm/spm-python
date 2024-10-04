from spm.__wrap__ import _Runtime


def _littleendian(*args, **kwargs):
  """  LITTLEENDIAN returns 1 (true) on a little endian machine, e.g. with an  
    Intel or AMD, or 0 (false) otherwise  
     
    Example  
      if (littleendian)  
        % do something, e.g. swap some bytes  
       end  
     
    See also BIGENDIAN, SWAPBYTES, TYPECAST  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/littleendian.m)
  """

  return _Runtime.call("littleendian", *args, **kwargs)
