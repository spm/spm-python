from spm._runtime import Runtime


def _menu_fieldtrip(*args, **kwargs):
    """
      MENU_FIELDTRIP adds a FieldTrip-specific menu to a figure.  
         
        See also MENU_VIEWPOINT  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/menu_fieldtrip.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("menu_fieldtrip", *args, **kwargs, nargout=0)
