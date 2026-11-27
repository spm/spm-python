from spm._runtime import Runtime


def _setsubfield(*args, **kwargs):
    r"""
      SETSUBFIELD sets the contents of the specified field to a specified value  
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
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/connectivity/private/setsubfield.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("setsubfield", *args, **kwargs)
