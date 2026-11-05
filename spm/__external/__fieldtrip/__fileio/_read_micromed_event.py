from spm._runtime import Runtime


def _read_micromed_event(*args, **kwargs):
    r"""
      reads the events of the Micromed TRC format files  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_micromed_event.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_micromed_event", *args, **kwargs)
