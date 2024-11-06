from spm.__wrapper__ import Runtime


def bf_output_montage(*args, **kwargs):
    """
      Generate a montage for source extraction  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_output_montage.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("bf_output_montage", *args, **kwargs)
