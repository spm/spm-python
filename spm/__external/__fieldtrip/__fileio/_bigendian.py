from spm.__wrap__ import _Runtime


def _bigendian(*args, **kwargs):
  """  BIGENDIAN returns 1 (true) on a big endian machine, e.g. with a SUN Sparc  
    or Apple G4 processor, or 0 (false) otherwise  
     
    Example  
      if (bigendian)  
        % do something, e.g. swap some bytes  
       end  
     
    See also LITTLEENDIAN, SWAPBYTES, TYPECAST  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/bigendian.m)
  """

  return _Runtime.call("bigendian", *args, **kwargs)
