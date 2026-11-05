from spm._runtime import Runtime


def _comp2timelock(*args, **kwargs):
    r"""
      COMP2TIMELOCK transform the independent components into something  
        on which the timelocked source reconstruction methods can  
        perform their trick.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/comp2timelock.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("comp2timelock", *args, **kwargs)
