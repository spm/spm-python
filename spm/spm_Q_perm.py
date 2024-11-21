from spm.__wrapper__ import Runtime


def spm_Q_perm(*args, **kwargs):
    """
      Return a cell of permutation indices for separating matrices  
        FORMAT p = spm_Q_perm(Q)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_Q_perm.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_Q_perm", *args, **kwargs)
