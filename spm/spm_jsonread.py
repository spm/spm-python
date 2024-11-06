from spm.__wrapper__ import Runtime


def spm_jsonread(*args, **kwargs):
    """
      JSON (JavaScript Object Notation) parser - a compiled routine  
        FORMAT json = spm_jsonread(filename, opts)  
        filename - name of a JSON file or JSON string  
        json     - JSON structure  
        opts     - structure or list of name/value pairs of optional parameters:  
                     ReplacementStyle: string to control how non-alphanumeric  
                       characters are replaced {'underscore','hex','delete','nop'}  
                       [Default: 'underscore']  
                     Prefix: string to prepend when first character of a field is  
                       not alphabetical [Default: 'x']  
          
        References:  
          JSON Standard: https://www.json.org/  
          JSMN C parser: https://zserge.com/jsmn/  
          jsondecode: https://www.mathworks.com/help/matlab/ref/jsondecode.html  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_jsonread.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_jsonread", *args, **kwargs)
