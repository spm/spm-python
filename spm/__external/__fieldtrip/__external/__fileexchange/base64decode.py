from spm._runtime import Runtime


def base64decode(*args, **kwargs):
    r"""
     BASE64DECODE Decode Base64 string to a byte array.  
         
           output = base64decode(input)  
         
        The function takes a Base64 string INPUT and returns a uint8 array  
        OUTPUT. JAVA must be running to use this function. The result is always  
        given as a 1-by-N array, and doesn't retrieve the original dimensions.  
         
        See also base64encode  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/external/fileexchange/base64decode.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("base64decode", *args, **kwargs)
