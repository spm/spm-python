from spm._runtime import Runtime


def _avgoverdim(*args, **kwargs):
    """
    avgoverdim is a function.  
          data = avgoverdim(data, avgdim, fb)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/avgoverdim.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("avgoverdim", *args, **kwargs)
