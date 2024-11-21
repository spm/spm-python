from spm.__wrapper__ import Runtime


def tinv(*args, **kwargs):
    """
      TINV   Inverse of Student's T cumulative distribution function (cdf).  
          X=TINV(P,V) returns the inverse of Student's T cdf with V degrees   
          of freedom, at the values in P.  
         
          The size of X is the common size of P and V. A scalar input     
          functions as a constant matrix of the same size as the other input.      
         
        This is an open source function that was assembled by Eric Maris using  
        open source subfunctions found on the web.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/external/stats/tinv.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("tinv", *args, **kwargs)
