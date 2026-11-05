from spm._runtime import Runtime


def _getsubfield(*args, **kwargs):
    r"""
      GETSUBFIELD returns a field from a structure just like the standard  
        GETFIELD function, except that you can also specify nested fields  
        using a '.' in the fieldname. The nesting can be arbitrary deep.  
         
        Use as  
          f = getsubfield(s, 'fieldname')  
        or as  
          f = getsubfield(s, 'fieldname.subfieldname')  
         
        See also GETFIELD, ISSUBFIELD, SETSUBFIELD  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/plotting/private/getsubfield.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("getsubfield", *args, **kwargs)
