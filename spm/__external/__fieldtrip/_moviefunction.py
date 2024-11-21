from spm.__wrapper__ import Runtime


def _moviefunction(*args, **kwargs):
    """
      we need cfg.plotfun to plot the data  
        data needs to be 3D, N x time x freq (last can be singleton)  
          N needs to correspond to number of vertices (channels, gridpoints, etc)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/moviefunction.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("moviefunction", *args, **kwargs, nargout=0)
