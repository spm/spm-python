from mpython import Runtime


def _read_nexstim_event(*args, **kwargs):
    """
      Use as
          [event] = read_nexstim_event(filename)


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_nexstim_event.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_nexstim_event", *args, **kwargs)
