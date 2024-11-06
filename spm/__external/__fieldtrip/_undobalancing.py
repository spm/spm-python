from spm.__wrapper__ import Runtime


def _undobalancing(*args, **kwargs):
    """
      UNDOBALANCING removes all balancing coefficients from the gradiometer sensor array  
         
        This is used in CHANNELPOSITION, FT_PREPARE_LAYOUT, FT_SENSTYPE  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/undobalancing.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("undobalancing", *args, **kwargs)
