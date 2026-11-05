from spm._runtime import Runtime


def tsss_config_momentspace(*args, **kwargs):
    r"""
      Configuration file for TSSS space conversion  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/TSSS/tsss_config_momentspace.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("tsss_config_momentspace", *args, **kwargs)
