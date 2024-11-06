from spm.__wrapper__ import Runtime


def _printand(*args, **kwargs):
    """
      PRINTAND prints a single or multiple strings as "x1, x2, x3 and x4". If there is  
        only one string, that string is returned without additional formatting.  
         
        See also PRINTOR  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/printand.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("printand", *args, **kwargs)
