from mpython import Runtime


def _smartinput(*args, **kwargs):
    """
      SMARTINPUT helper function for smart interactive input from the command line

        Use as
          [newval, change] = smartinput(question, oldval)

        See also INPUT, PAUSE


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/smartinput.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("smartinput", *args, **kwargs)
