from spm.__wrapper__ import Runtime


def spm_freqs(*args, **kwargs):
    """
     FREQS Laplace-transform (s-domain) frequency response.    
          H = FREQS(B,A,W) returns the complex frequency response vector H   
          of the filter B/A:  
                               nb-1         nb-2  
                   B(s)   b(1)s     +  b(2)s     + ... +  b(nb)  
            H(s) = ---- = -------------------------------------  
                               na-1         na-2  
                   A(s)   a(1)s     +  a(2)s     + ... +  a(na)  
         
          given the numerator and denominator coefficients in vectors B and A.   
          The frequency response is evaluated at the points specified in   
          vector W (in rad/s).  The magnitude and phase can be graphed by  
          calling FREQS(B,A,W) with no output arguments.  
         
          [H,W] = FREQS(B,A) automatically picks a set of 200 frequencies W on   
          which the frequency response is computed.  FREQS(B,A,N) picks N   
          frequencies.   
         
          See also LOGSPACE, POLYVAL, INVFREQS, and FREQZ.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Neural_Models/spm_freqs.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_freqs", *args, **kwargs)
