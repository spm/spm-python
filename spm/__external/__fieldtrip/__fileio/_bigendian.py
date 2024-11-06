from spm.__wrapper__ import Runtime


def _bigendian(*args, **kwargs):
    """
      BIGENDIAN returns 1 (true) on a big endian machine, e.g. with a SUN Sparc  
        or Apple G4 processor, or 0 (false) otherwise  
         
        Example  
          if (bigendian)  
            % do something, e.g. swap some bytes  
           end  
         
        See also LITTLEENDIAN, SWAPBYTES, TYPECAST  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/bigendian.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("bigendian", *args, **kwargs)
