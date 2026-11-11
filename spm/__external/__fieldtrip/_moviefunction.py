from spm._runtime import Runtime


def _moviefunction(*args, **kwargs):
    r"""
      we need cfg.plotfun to plot the data  
        data needs to be 3D, N x time x freq (last can be singleton)  
          N needs to correspond to number of vertices (channels, gridpoints, etc)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/moviefunction.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("moviefunction", *args, **kwargs, nargout=0)
