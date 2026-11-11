from spm._runtime import Runtime


def spm_betaln(*args, **kwargs):
    r"""
      Logarithm of the multivariate beta function of a vector  
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
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_betaln.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_betaln", *args, **kwargs)
