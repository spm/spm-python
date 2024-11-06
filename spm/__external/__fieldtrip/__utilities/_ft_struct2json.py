from spm.__wrapper__ import Runtime


def _ft_struct2json(*args, **kwargs):
    """
       FT_STRUCT2JSON  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/ft_struct2json.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_struct2json", *args, **kwargs)
