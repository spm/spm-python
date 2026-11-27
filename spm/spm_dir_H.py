from spm._runtime import Runtime


def spm_dir_H(*args, **kwargs):
    r"""
      Entropy of a Dirichlet distribution  
        FORMAT H = spm_dir_H(a)  
        a    - Dirichlet parameters of a joint distribution  
        H    - Entropy  
         
        The entropy here pertains to the Dirichlet distribution.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_dir_H.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_dir_H", *args, **kwargs)
