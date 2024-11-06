from spm.__wrapper__ import Runtime


def keepfields(*args, **kwargs):
    """
      KEEPFIELDS makes a selection of the fields in a structure  
         
        Use as  
          s = keepfields(s, fields);  
         
        See also REMOVEFIELDS, COPYFIELDS  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/keepfields.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("keepfields", *args, **kwargs)
