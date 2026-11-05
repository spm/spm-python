from spm._runtime import Runtime


def _jaga16_packet(*args, **kwargs):
    r"""
      JAGA16_PACKET converts the JAGA16 byte stream into packets  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/jaga16_packet.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("jaga16_packet", *args, **kwargs)
