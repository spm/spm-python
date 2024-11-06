from spm.__wrapper__ import Runtime


def newline(*args, **kwargs):
    """
      NEWLINE Create newline character  
          C = newline creates the character representing a newline.  
          newline is equivalent to char(10) or sprintf('
    ').  
         
        This is a compatibility function that should only be added to the path on  
        MATLAB versions prior to R2016b.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/compat/matlablt2016b/newline.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("newline", *args, **kwargs)
