from spm.__wrapper__ import Runtime


def _read_wdq_header(*args, **kwargs):
    """
      READ_WDQ_HEADER reads header information from wdq files  
         
        Use as  
         [hdr] = read_wdq_header(filename)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_wdq_header.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_wdq_header", *args, **kwargs)
