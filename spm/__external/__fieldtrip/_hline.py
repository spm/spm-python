from spm.__wrapper__ import Runtime


def _hline(*args, **kwargs):
    """
      HLINE plot a horizontal line in the current graph  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/hline.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("hline", *args, **kwargs, nargout=0)
