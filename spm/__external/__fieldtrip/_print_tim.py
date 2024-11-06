from spm.__wrapper__ import Runtime


def _print_tim(*args, **kwargs):
    """
      SUBFUNCTION for pretty-printing time in hours, minutes, ...  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/print_tim.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("print_tim", *args, **kwargs)
