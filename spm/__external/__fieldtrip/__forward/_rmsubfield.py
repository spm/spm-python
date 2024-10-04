from spm.__wrap__ import _Runtime


def _rmsubfield(*args, **kwargs):
  """  RMSUBFIELD removes the contents of the specified field from a structure  
    just like the standard Matlab RMFIELD function, except that you can also  
    specify nested fields using a '.' in the fieldname. The nesting can be  
    arbitrary deep.  
     
    Use as  
      s = rmsubfield(s, 'fieldname')  
    or as  
      s = rmsubfield(s, 'fieldname.subfieldname')  
     
    See also SETFIELD, GETSUBFIELD, ISSUBFIELD  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/forward/private/rmsubfield.m)
  """

  return _Runtime.call("rmsubfield", *args, **kwargs)
