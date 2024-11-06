from spm.__wrapper__ import Runtime


def bf_group_batch(*args, **kwargs):
    """
      Run a DAiSS batch on a group of subjects  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_group_batch.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("bf_group_batch", *args, **kwargs)
