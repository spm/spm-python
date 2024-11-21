from spm.__wrapper__ import Runtime


def bf_output_image_filtcorr(*args, **kwargs):
    """
      Computes filter correlation images  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_output_image_filtcorr.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("bf_output_image_filtcorr", *args, **kwargs)
