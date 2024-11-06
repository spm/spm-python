from spm.__wrapper__ import Runtime


def bf_regularise_tichonov_rankdef(*args, **kwargs):
    """
      Tichonov regularisation for rank deficient matrices based on the function  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_regularise_tichonov_rankdef.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("bf_regularise_tichonov_rankdef", *args, **kwargs)
