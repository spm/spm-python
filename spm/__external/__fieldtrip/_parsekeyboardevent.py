from spm._runtime import Runtime


def _parsekeyboardevent(*args, **kwargs):
    """
      PARSEKEYBOARDEVENT handles keyboard events for Windows, Mac OSX and Linux systems.  
         
        shift+numpad number does not work on UNIX, since the shift modifier is always sent for numpad events  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/parsekeyboardevent.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("parsekeyboardevent", *args, **kwargs)
