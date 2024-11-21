from spm.__wrapper__ import Runtime


def spm_jsonwrite(*args, **kwargs):
    """
      Serialize a JSON (JavaScript Object Notation) structure  
        FORMAT spm_jsonwrite(filename,json)  
        filename - JSON filename  
        json     - JSON structure  
         
        FORMAT S = spm_jsonwrite(json)  
        json     - JSON structure  
        S        - serialized JSON structure (string)  
         
        FORMAT [...] = spm_jsonwrite(...,opts)  
        opts     - structure or list of name/value pairs of optional parameters:  
                     prettyPrint: indent output [Default: false]  
                     replacementStyle: string to control how non-alphanumeric  
                       characters are replaced {'underscore','hex','delete','nop'}  
                       [Default: 'underscore']  
                     convertInfAndNaN: encode NaN, Inf and -Inf as "null"  
                       [Default: true]  
          
        References:  
          JSON Standard: https://www.json.org/  
          jsonencode: https://www.mathworks.com/help/matlab/ref/jsonencode.html  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_jsonwrite.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_jsonwrite", *args, **kwargs)
