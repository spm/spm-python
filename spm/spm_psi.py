from spm.__wrapper__ import Runtime


def spm_psi(*args, **kwargs):
    """
      Normalisation of a Dirichlet probability matrix (columns)  
        FORMAT [A] = spm_psi(a)  
         
        a  - Dirichlet parameter tensor  
         
        This can be regarded as log(spm_dir_norm(a)). More formally, it  
        corresponds to  the expectation  of the log marginals: E[log(X)]: X(i)  
        ~ Beta(a(i),a0 - a(i)). See also: psi.m  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_psi.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_psi", *args, **kwargs)
