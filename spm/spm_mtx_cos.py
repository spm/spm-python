from spm.__wrapper__ import Runtime


def spm_mtx_cos(*args, **kwargs):
    """
      returns the cosine of the angle between A and B  
        FORMAT c = spm_mtx_cos(A,B)  
         
        a    - (Dirichlet) parameters of a conditional probability matrix  
         
        c = arccos( <A|B> /(<A|A><B|B>))  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_mtx_cos.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mtx_cos", *args, **kwargs)
