from spm._runtime import Runtime


def spm_multrnd(*args, **kwargs):
    r"""
      Sample from multinomial distribution  
        FORMAT [m] = spm_multrnd(p,N)  
         
        p    - [M x 1] vector of probabilities  
        N    - Number of samples to generate  
          
        m    - [N x 1] vector of samples, where each sample is number from 1 to M  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_multrnd.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_multrnd", *args, **kwargs)
