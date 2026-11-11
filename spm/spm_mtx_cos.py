from spm._runtime import Runtime


def spm_mtx_cos(*args, **kwargs):
    r"""
      returns the cosine of the angle between A and B  
        FORMAT c = spm_mtx_cos(A,B)  
         
        a    - (Dirichlet) parameters of a conditional probability matrix  
         
        c = arccos( <A|B> /(<A|A><B|B>))  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_mtx_cos.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mtx_cos", *args, **kwargs)
