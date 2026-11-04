from spm._runtime import Runtime


def _bigendian(*args, **kwargs):
    r"""
      BIGENDIAN returns 1 (true) on a big endian machine, e.g. with a SUN Sparc  
        or Apple G4 processor, or 0 (false) otherwise  
         
        Example  
          if (bigendian)  
            % do something, e.g. swap some bytes  
           end  
         
        See also LITTLEENDIAN, SWAPBYTES, TYPECAST  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/bigendian.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("bigendian", *args, **kwargs)
