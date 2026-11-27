from spm._runtime import Runtime


def _parsekeyboardevent(*args, **kwargs):
    r"""
      PARSEKEYBOARDEVENT handles keyboard events for Windows, Mac OSX and Linux systems.  
         
        shift+numpad number does not work on UNIX, since the shift modifier is always sent for numpad events  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/parsekeyboardevent.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("parsekeyboardevent", *args, **kwargs)
