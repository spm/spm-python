from spm._runtime import Runtime


def issubfield(*args, **kwargs):
    r"""
      ISSUBFIELD tests for the presence of a field in a structure just like the standard  
        Matlab ISFIELD function, except that you can also specify nested fields  
        using a '.' in the fieldname. The nesting can be arbitrary deep.  
         
        Use as  
          f = issubfield(s, 'fieldname')  
        or as  
          f = issubfield(s, 'fieldname.subfieldname')  
         
        This function returns true if the field is present and false if the field  
        is not present.  
         
        See also ISFIELD, GETSUBFIELD, SETSUBFIELD  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/utilities/issubfield.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("issubfield", *args, **kwargs)
