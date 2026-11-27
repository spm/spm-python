from spm._runtime import Runtime


def splint_gh(*args, **kwargs):
    r"""
      SPLINT_GH implements equations (3) and (5b) of Perrin 1989  
        for simultaneous computation of multiple values  
         
        Use as  
          [gx, hx] = splint_gh(x)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/src/splint_gh.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("splint_gh", *args, **kwargs)
