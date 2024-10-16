from spm.__wrapper__ import Runtime


def _parsekeyboardevent(*args, **kwargs):
  """  PARSEKEYBOARDEVENT handles keyboard events for Windows, Mac OSX and Linux systems.  
     
    shift+numpad number does not work on UNIX, since the shift modifier is always sent for numpad events  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/parsekeyboardevent.m)
  """

  return Runtime.call("parsekeyboardevent", *args, **kwargs)
