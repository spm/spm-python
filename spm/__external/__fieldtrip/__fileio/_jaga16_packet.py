from mpython import Runtime


def _jaga16_packet(*args, **kwargs):
    """
      JAGA16_PACKET converts the JAGA16 byte stream into packets


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/jaga16_packet.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("jaga16_packet", *args, **kwargs)
