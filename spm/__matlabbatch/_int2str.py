from spm.__wrapper__ import Runtime


def _int2str(*args, **kwargs):
    """
     INT2STR Convert integer to string.  
          S = INT2STR(X) rounds the elements of the matrix X to  
          integers and converts the result into a string matrix.  
          Return NaN and Inf elements as strings 'NaN' and 'Inf', respectively.  
         
          Modified by Volkmar Glauche to return 'true' and 'false' instead of 0  
          and 1 for logical arrays.  
         
          See also NUM2STR, SPRINTF, FPRINTF, MAT2STR.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/private/int2str.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("int2str", *args, **kwargs)
