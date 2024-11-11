from spm.__wrapper__ import Runtime


def _rejectvisual_summary(*args, **kwargs):
    """
      SUBFUNCTION for ft_rejectvisual  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/rejectvisual_summary.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("rejectvisual_summary", *args, **kwargs)
