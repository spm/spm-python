from spm._runtime import Runtime


def _setsubfield(*args, **kwargs):
    """
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/setsubfield.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("setsubfield", *args, **kwargs)
