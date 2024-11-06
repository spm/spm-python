from spm.__wrapper__ import Runtime


def spm_axis(*args, **kwargs):
    """
      AXIS  Control axis scaling and appearance.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_axis.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_axis", *args, **kwargs)
