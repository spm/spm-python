from spm.__wrapper__ import Runtime


def _read_micromed_event(*args, **kwargs):
    """
      reads the events of the Micromed TRC format files  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_micromed_event.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_micromed_event", *args, **kwargs)
