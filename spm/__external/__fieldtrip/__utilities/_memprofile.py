from spm.__wrapper__ import Runtime


def _memprofile(*args, **kwargs):
    """
      MEMPROFILE this is a dummy placeholder  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/memprofile.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("memprofile", *args, **kwargs)
