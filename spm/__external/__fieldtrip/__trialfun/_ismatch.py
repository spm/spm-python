from spm.__wrapper__ import Runtime


def _ismatch(*args, **kwargs):
    """
      ISMATCH returns true if x is a member of array y, regardless of the class  
        of x and y, if y is a string, or a cell-array of strings, it can contain  
        the wildcard '*'  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/trialfun/private/ismatch.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ismatch", *args, **kwargs)
