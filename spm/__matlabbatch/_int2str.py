from spm.__wrap__ import _Runtime


def _int2str(*args, **kwargs):
  """ INT2STR Convert integer to string.  
      S = INT2STR(X) rounds the elements of the matrix X to  
      integers and converts the result into a string matrix.  
      Return NaN and Inf elements as strings 'NaN' and 'Inf', respectively.  
     
      Modified by Volkmar Glauche to return 'true' and 'false' instead of 0  
      and 1 for logical arrays.  
     
      See also NUM2STR, SPRINTF, FPRINTF, MAT2STR.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/matlabbatch/private/int2str.m)
  """

  return _Runtime.call("int2str", *args, **kwargs)
