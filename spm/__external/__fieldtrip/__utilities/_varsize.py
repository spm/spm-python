from spm.__wrapper__ import Runtime


def _varsize(*args, **kwargs):
    """
      VARSIZE returns the size of a variable in bytes. It can be used on any MATLAB  
        variable, including structures and cell arrays.  
         
        See also WHOS  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/varsize.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("varsize", *args, **kwargs)
