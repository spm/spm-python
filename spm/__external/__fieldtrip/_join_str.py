from spm.__wrapper__ import Runtime


def _join_str(*args, **kwargs):
    """
    join_str is a function.  
          t = join_str(separator, cells)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/join_str.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("join_str", *args, **kwargs)
