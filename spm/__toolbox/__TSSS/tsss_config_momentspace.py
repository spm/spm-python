from spm.__wrapper__ import Runtime


def tsss_config_momentspace(*args, **kwargs):
    """
      Configuration file for TSSS space conversion  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/TSSS/tsss_config_momentspace.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("tsss_config_momentspace", *args, **kwargs)
