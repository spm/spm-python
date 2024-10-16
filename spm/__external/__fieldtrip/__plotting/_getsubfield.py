from spm.__wrapper__ import Runtime


def _getsubfield(*args, **kwargs):
  """  GETSUBFIELD returns a field from a structure just like the standard  
    GETFIELD function, except that you can also specify nested fields  
    using a '.' in the fieldname. The nesting can be arbitrary deep.  
     
    Use as  
      f = getsubfield(s, 'fieldname')  
    or as  
      f = getsubfield(s, 'fieldname.subfieldname')  
     
    See also GETFIELD, ISSUBFIELD, SETSUBFIELD  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/plotting/private/getsubfield.m)
  """

  return Runtime.call("getsubfield", *args, **kwargs)
