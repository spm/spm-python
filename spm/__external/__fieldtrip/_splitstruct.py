from spm.__wrapper__ import Runtime


def _splitstruct(*args, **kwargs):
    """
      SPLITSTRUCT splits a structure into names and values  
         
        See also PRINTSTRUCT  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/splitstruct.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("splitstruct", *args, **kwargs)
