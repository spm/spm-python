from spm._runtime import Runtime


def _read_nexstim_event(*args, **kwargs):
    r"""
      Use as  
          [event] = read_nexstim_event(filename)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_nexstim_event.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_nexstim_event", *args, **kwargs)
