from spm.__wrapper__ import Runtime


def istrue(*args, **kwargs):
  """  ISTRUE converts an input argument like "yes/no", "true/false" or "on/off" into a  
    boolean. If the input is boolean, then it will remain like that.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/istrue.m)
  """

  return Runtime.call("istrue", *args, **kwargs)
