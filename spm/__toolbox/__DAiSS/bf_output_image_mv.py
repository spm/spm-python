from spm.__wrapper__ import Runtime


def bf_output_image_mv(*args, **kwargs):
    """
      Compute multivariate test on a number of frequency bands  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_output_image_mv.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("bf_output_image_mv", *args, **kwargs)
