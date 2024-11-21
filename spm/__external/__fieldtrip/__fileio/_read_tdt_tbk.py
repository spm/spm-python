from spm.__wrapper__ import Runtime


def _read_tdt_tbk(*args, **kwargs):
    """
      tbk file has block events information and time marks  
        for efficiently locate event if query by time  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_tdt_tbk.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_tdt_tbk", *args, **kwargs)
