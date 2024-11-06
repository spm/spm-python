from spm.__wrapper__ import Runtime


def bf_output_image_sensitivity(*args, **kwargs):
    """
      Sensitivity profile for a group of sensors  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_output_image_sensitivity.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("bf_output_image_sensitivity", *args, **kwargs)
