from spm._runtime import Runtime


def spm_mldivide(*args, **kwargs):
    r"""
      Regularised variant of mldivide(A, B) or A \ B, similar to spm_inv(A) * B  
        FORMAT D = spm_mldivide(A, B)  
         
        D = inv(A) * B, or if A is near singular D = inv(A + TOL*eye(size(A)) * B  
          
        where TOL is adaptively increased if necessary.  
         
        This function should be preferable to spm_inv(A) * B if A is large and  
        sparse or if B has few columns, since the inverse need not be explicitly  
        computed (the linear system can be solved with the backslash operator).  
         
        See also: spm_mrdivide  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_mldivide.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mldivide", *args, **kwargs)
