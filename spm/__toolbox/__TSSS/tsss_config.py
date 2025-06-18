from mpython import Runtime


def tsss_config(*args, **kwargs):
    """
      Configuration file for TSSS clean-up for Neuromag data
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/TSSS/tsss_config.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("tsss_config", *args, **kwargs)
