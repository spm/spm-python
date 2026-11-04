from spm._runtime import Runtime


def _menu_fieldtrip(*args, **kwargs):
    r"""
      MENU_FIELDTRIP adds a FieldTrip-specific menu to a figure.  
         
        See also MENU_VIEWPOINT  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/menu_fieldtrip.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("menu_fieldtrip", *args, **kwargs, nargout=0)
