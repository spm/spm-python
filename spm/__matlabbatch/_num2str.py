from spm.__wrapper__ import Runtime


def _num2str(*args, **kwargs):
    """
     NUM2STR Convert numbers to a string.  
          T = NUM2STR(X) converts the matrix X into a string representation T  
          with about 4 digits and an exponent if required.  This is useful for  
          labeling plots with the TITLE, XLABEL, YLABEL, and TEXT commands.  
         
          T = NUM2STR(X,N) converts the matrix X into a string representation  
          with a maximum N digits of precision.  The default number of digits is  
          based on the magnitude of the elements of X.  
         
          T = NUM2STR(X,FORMAT) uses the format string FORMAT (see SPRINTF for  
          details).  
         
          If the input array is integer-valued, num2str returns the exact string  
          representation of that integer. The term integer-valued includes large  
          floating-point numbers that lose precision due to limitations of the   
          hardware.  
         
          Example:  
              num2str(randn(2,2),3) produces the string matrix  
         
              '-0.433    0.125'  
              ' -1.67    0.288'  
         
          See also INT2STR, SPRINTF, FPRINTF, MAT2STR.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/private/num2str.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("num2str", *args, **kwargs)
