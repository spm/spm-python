from spm.__wrapper__ import Runtime


def spm_mldivide(*args, **kwargs):
    """
      Regularised variant of mldivide(A, B) or A \ B, similar to spm_inv(A) * B  
        FORMAT D = spm_mldivide(A, B)  
         
        D = inv(A) * B, or if A is near singular D = inv(A + TOL*eye(size(A)) * B  
          
        where TOL is adaptively increased if necessary.  
         
        This function should be preferable to spm_inv(A) * B if A is large and  
        sparse or if B has few columns, since the inverse need not be explicitly  
        computed (the linear system can be solved with the backslash operator).  
         
        See also: spm_mrdivide  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_mldivide.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mldivide", *args, **kwargs)
