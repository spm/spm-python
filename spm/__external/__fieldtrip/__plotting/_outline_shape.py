from spm._runtime import Runtime


def _outline_shape(*args, **kwargs):
    r"""
      helper function for ft_prepare_layout and ft_plot_topo to create an  
        outline (to-be-plotted), or a mask (to use as extrapolation boundary).  
        The input is either a layout structure, or an Nx2 matrix with point  
        positions.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/plotting/private/outline_shape.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("outline_shape", *args, **kwargs)
