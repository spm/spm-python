from spm._runtime import Runtime


def ft_select_box(*args, **kwargs):
    r"""
      FT_SELECT_BOX helper function for selecting a single rectangular region in the  
        current figure using the mouse. This function is not used as a callback, but blocks  
        the execution of the code until a selection is made.  
         
        Use as  
          [x, y] = ft_select_box()  
         
        It returns a 2-element vector x and a 2-element vector y  
        with the corners of the selected region.  
         
        See also FT_SELECT_CHANNEL, FT_SELECT_POINT, FT_SELECT_POINT3D, FT_SELECT_RANGE,  
        FT_SELECT_VOXEL, GINPUT, RBBOX  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/plotting/ft_select_box.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_select_box", *args, **kwargs)
