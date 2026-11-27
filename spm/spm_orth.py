from spm._runtime import Runtime


def spm_orth(*args, **kwargs):
    r"""
      Recursive Gram-Schmidt orthogonalisation of basis functions  
        FORMAT X = spm_orth(X,OPT)  
         
        X   - matrix  
        OPT - 'norm' for Euclidean normalisation  
            - 'pad'  for zero padding of null space [default]  
         
        Serial orthogonalisation starting with the first column  
         
        Reference:  
        Golub, Gene H. & Van Loan, Charles F. (1996), Matrix Computations (3rd  
        ed.), Johns Hopkins, ISBN 978-0-8018-5414-9.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_orth.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_orth", *args, **kwargs)
