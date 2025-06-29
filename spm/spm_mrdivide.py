from spm._runtime import Runtime


def spm_mrdivide(*args, **kwargs):
    """
      Regularised variant of mrdivide(A, B) or A / B, similar to B * spm_inv(A)  
        FORMAT D = spm_mrdivide(A, B)  
         
        D = B * inv(A), or if A is near singular D = B * inv(A + TOL*eye(size(A))  
          
        where TOL is adaptively increased if necessary.  
         
        This function should be preferable to B * spm_inv(A) if A is large and  
        sparse or if B has few rows, since the inverse need not be explicitly  
        computed (the linear system can be solved with the backslash operator).  
         
        See also: spm_mldivide  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_mrdivide.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mrdivide", *args, **kwargs)
