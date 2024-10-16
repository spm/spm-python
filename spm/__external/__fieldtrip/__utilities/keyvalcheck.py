from spm.__wrapper__ import Runtime


def keyvalcheck(*args, **kwargs):
  """  KEYVALCHECK is a helper function for parsing optional key-value input pairs.  
     
    Use as  
      keyvalcheck(argin, 'required',  {'key1', 'key2', ...})  
      keyvalcheck(argin, 'forbidden', {'key1', 'key2', ...})  
      keyvalcheck(argin, 'optional',  {'key1', 'key2', ...})  
     
    See also KEYVAL  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/keyvalcheck.m)
  """

  return Runtime.call("keyvalcheck", *args, **kwargs, nargout=0)
