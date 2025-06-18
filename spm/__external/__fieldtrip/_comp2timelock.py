from mpython import Runtime


def _comp2timelock(*args, **kwargs):
    """
      COMP2TIMELOCK transform the independent components into something
        on which the timelocked source reconstruction methods can
        perform their trick.


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/comp2timelock.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("comp2timelock", *args, **kwargs)
