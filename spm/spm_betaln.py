from spm.__wrap__ import _Runtime


def spm_betaln(*args, **kwargs):
  """  Logarithm of the multivariate beta function of a vector  
    FORMAT y = spm_betaln(z)  
      y = spm_betaln(z) computes the natural logarithm of the beta function  
      for corresponding elements of the vector z. if z is an array, the beta  
      functions are taken over the elements of the first dimension (and  
      size(y,1) equals one).  
     
      See also BETAINC, BETA.  
   --------------------------------------------------------------------------  
      Ref: Abramowitz & Stegun, Handbook of Mathematical Functions, sec. 6.2.  
      Copyright 1984-2004 The MathWorks, Inc.   
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_betaln.m)
  """

  return _Runtime.call("spm_betaln", *args, **kwargs)
