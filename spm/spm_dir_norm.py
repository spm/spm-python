from spm._runtime import Runtime


def spm_dir_norm(*args, **kwargs):
    """
      Normalisation of a (Dirichlet) conditional probability matrix  
        FORMAT A = spm_dir_norm(a)  
         
        a    - (Dirichlet) parameters of a conditional probability matrix  
         
        A    - conditional probability matrix  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dir_norm.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_dir_norm", *args, **kwargs)
