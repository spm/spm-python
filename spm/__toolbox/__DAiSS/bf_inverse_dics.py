from spm.__wrapper__ import Runtime


def bf_inverse_dics(*args, **kwargs):
    """
      Computes DICS filters  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_inverse_dics.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("bf_inverse_dics", *args, **kwargs)
