from spm.__wrapper__ import Runtime


def _megplanar_sincos(*args, **kwargs):
    """
      This attempts to re-implements Ole's method, exept that the definition of the  
        horizontal and vertical direction is different.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/megplanar_sincos.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("megplanar_sincos", *args, **kwargs)
