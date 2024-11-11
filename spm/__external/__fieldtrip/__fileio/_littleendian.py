from spm.__wrapper__ import Runtime


def _littleendian(*args, **kwargs):
    """
      LITTLEENDIAN returns 1 (true) on a little endian machine, e.g. with an  
        Intel or AMD, or 0 (false) otherwise  
         
        Example  
          if (littleendian)  
            % do something, e.g. swap some bytes  
           end  
         
        See also BIGENDIAN, SWAPBYTES, TYPECAST  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/littleendian.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("littleendian", *args, **kwargs)
