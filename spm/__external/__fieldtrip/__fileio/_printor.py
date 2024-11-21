from spm.__wrapper__ import Runtime


def _printor(*args, **kwargs):
    """
      PRINTOR prints a single or multiple strings as "x1, x2, x3 or x4". If there is  
        only one string, that string is returned without additional formatting.  
         
        See also PRINTAND  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/printor.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("printor", *args, **kwargs)
