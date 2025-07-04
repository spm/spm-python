from spm._runtime import Runtime


def _rmsubfield(*args, **kwargs):
    """
      RMSUBFIELD removes the contents of the specified field from a structure  
        just like the standard Matlab RMFIELD function, except that you can also  
        specify nested fields using a '.' in the fieldname. The nesting can be  
        arbitrary deep.  
         
        Use as  
          s = rmsubfield(s, 'fieldname')  
        or as  
          s = rmsubfield(s, 'fieldname.subfieldname')  
         
        See also SETFIELD, GETSUBFIELD, ISSUBFIELD  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/rmsubfield.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("rmsubfield", *args, **kwargs)
