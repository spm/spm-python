from spm._runtime import Runtime


def common_size(*args, **kwargs):
    """
    common_size is a function.  
          [errorcode, varargout] = common_size(varargin)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/external/stats/common_size.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("common_size", *args, **kwargs)
