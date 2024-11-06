from spm.__wrapper__ import Runtime


def splint_gh(*args, **kwargs):
    """
      SPLINT_GH implements equations (3) and (5b) of Perrin 1989  
        for simultaneous computation of multiple values  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/src/splint_gh.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("splint_gh", *args, **kwargs)
