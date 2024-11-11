from spm.__wrapper__ import Runtime


def spm_orth(*args, **kwargs):
    """
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_orth.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_orth", *args, **kwargs)
