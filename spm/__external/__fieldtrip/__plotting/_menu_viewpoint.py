from spm.__wrapper__ import Runtime


def _menu_viewpoint(*args, **kwargs):
    """
      MENU_VIEWPOINT adds a context menu to a 3D figure.  
         
        See also MENU_FIELDTRIP  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/plotting/private/menu_viewpoint.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("menu_viewpoint", *args, **kwargs, nargout=0)
