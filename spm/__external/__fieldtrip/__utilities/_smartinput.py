from spm.__wrap__ import _Runtime


def _smartinput(*args, **kwargs):
  """  SMARTINPUT helper function for smart interactive input from the command line  
     
    Use as  
      [newval, change] = smartinput(question, oldval)  
     
    See also INPUT, PAUSE  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/smartinput.m)
  """

  return _Runtime.call("smartinput", *args, **kwargs)
