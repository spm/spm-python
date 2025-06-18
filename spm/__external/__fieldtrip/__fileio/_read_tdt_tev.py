from mpython import Runtime


def _read_tdt_tev(*args, **kwargs):
    """
      READ_TDT_TANK

        Use as
          [tev, tsq] = read_tdt_tank(filename)

        Note:
          tev file contains event binary data
          tev and tsq files work together to get an event's data and attributes
          sev files contains streamed binary data


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_tdt_tev.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_tdt_tev", *args, **kwargs)
