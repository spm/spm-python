from spm.__wrapper__ import Runtime


def ft_checkopt(*args, **kwargs):
    """
      FT_CHECKOPT does a validity test on the types and values of a configuration  
        structure or cell-array with key-value pairs.  
         
        Use as  
          opt = ft_checkopt(opt, key)  
          opt = ft_checkopt(opt, key, allowedtype)  
          opt = ft_checkopt(opt, key, allowedtype, allowedval)  
         
        For allowedtype you can specify a string or a cell-array with multiple  
        strings. All the default MATLAB types can be specified, such as  
          'double'  
          'logical'  
          'char'  
          'single'  
          'float'  
          'int16'  
          'cell'  
          'struct'  
          'function_handle'  
         
        Furthermore, the following custom types can be specified  
          'empty'  
          'doublescalar'  
          'doublevector'  
          'doublebivector'             i.e. [1 1] or [1 2]  
          'ascendingdoublevector'      i.e. [1 2 3 4 5], but not [1 3 2 4 5]  
          'ascendingdoublebivector'    i.e. [1 2], but not [2 1]  
          'doublematrix'  
          'numericscalar'  
          'numericvector'  
          'numericmatrix'  
          'charcell'  
         
        For allowedval you can specify a single value or a cell-array  
        with multiple values.  
         
        This function will give an error or it returns the input configuration  
        structure or cell-array without modifications. A match on any of the  
        allowed types and any of the allowed values is sufficient to let this  
        function pass.  
         
        See also FT_GETOPT, FT_SETOPT  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/ft_checkopt.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_checkopt", *args, **kwargs)
