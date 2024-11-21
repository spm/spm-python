from spm.__wrapper__ import Runtime


def bf_view_surface(*args, **kwargs):
    """
      Diplay surface plot of DAISS output results  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_view_surface.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("bf_view_surface", *args, **kwargs)
