from spm.__wrapper__ import Runtime


def _megplanar_orig(*args, **kwargs):
    """
      This is the original method from Ole.  It has a different way of  
        making the coordinate transformation that I do not fully understand.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/megplanar_orig.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("megplanar_orig", *args, **kwargs)
