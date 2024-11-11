from spm.__wrapper__ import Runtime


def _seloverdim(*args, **kwargs):
    """
    seloverdim is a function.  
          data = seloverdim(data, seldim, sel, fb)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/seloverdim.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("seloverdim", *args, **kwargs)
