from spm._runtime import Runtime


def spm_axis(*args, **kwargs):
    """
      AXIS  Control axis scaling and appearance.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_axis.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_axis", *args, **kwargs)
