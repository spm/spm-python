from spm.__wrapper__ import Runtime


def _avgoverlabel(*args, **kwargs):
    """
    avgoverlabel is a function.  
          str = avgoverlabel(label)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/avgoverlabel.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("avgoverlabel", *args, **kwargs)
