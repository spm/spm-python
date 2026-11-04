from spm._runtime import Runtime


def _menu_viewpoint(*args, **kwargs):
    r"""
      MENU_VIEWPOINT adds a context menu to a 3D figure.  
         
        See also MENU_FIELDTRIP  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/plotting/private/menu_viewpoint.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("menu_viewpoint", *args, **kwargs, nargout=0)
