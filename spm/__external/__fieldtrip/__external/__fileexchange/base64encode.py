from spm._runtime import Runtime


def base64encode(*args, **kwargs):
    r"""
     BASE64ENCODE Encode a byte array using Base64 codec.  
         
           output = base64encode(input)  
         
        The function takes a char, int8, or uint8 array INPUT and returns Base64  
        encoded string OUTPUT. JAVA must be running to use this function. Note  
        that encoding doesn't preserve input dimensions.  
         
        See also base64decode  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/external/fileexchange/base64encode.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("base64encode", *args, **kwargs)
