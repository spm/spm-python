from spm.__wrapper__ import Runtime


def setsubfield(*args, **kwargs):
  """  SETSUBFIELD sets the contents of the specified field to a specified value  
    just like the standard Matlab SETFIELD function, except that you can also  
    specify nested fields using a '.' in the fieldname. The nesting can be  
    arbitrary deep.  
     
    Use as  
      s = setsubfield(s, 'fieldname', value)  
    or as  
      s = setsubfield(s, 'fieldname.subfieldname', value)  
     
    where nested is a logical, false denoting that setsubfield will create  
    s.subfieldname instead of s.fieldname.subfieldname  
     
    See also SETFIELD, GETSUBFIELD, ISSUBFIELD  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/setsubfield.m)
  """

  return Runtime.call("setsubfield", *args, **kwargs)
