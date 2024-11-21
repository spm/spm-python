from spm.__wrapper__ import Runtime


def bf_copy(*args, **kwargs):
    """
      Set up a new analysis by copying an existing one  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_copy.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("bf_copy", *args, **kwargs)
