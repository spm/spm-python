from spm.__wrapper__ import Runtime


def bf_std_fields(*args, **kwargs):
    """
       
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_std_fields.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("bf_std_fields", *args, **kwargs)
