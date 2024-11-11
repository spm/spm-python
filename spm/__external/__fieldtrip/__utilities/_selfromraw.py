from spm.__wrapper__ import Runtime


def _selfromraw(*args, **kwargs):
    """
      FIXME this function is not documented  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/selfromraw.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("selfromraw", *args, **kwargs)
