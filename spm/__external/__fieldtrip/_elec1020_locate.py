from spm.__wrapper__ import Runtime


def _elec1020_locate(*args, **kwargs):
    """
      ELEC1020_LOCATE determines 10-20 (20%, 10% and 5%) electrode positions  
        on a scalp surface that is described by its surface triangulation  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/elec1020_locate.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("elec1020_locate", *args, **kwargs)
