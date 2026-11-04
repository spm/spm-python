from spm._runtime import Runtime


def _read_tdt_tsq(*args, **kwargs):
    r"""
      READ_TDT_TSQ reads the headers from a Tucker_Davis_technologies TSQ file  
         
        tsq file is a heap of event headers, which is ?40 byte each,  
        ordered strictly by time  
         
        Use as  
          tsq = read_tdt_tsq(filename, begblock, endblock)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_tdt_tsq.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_tdt_tsq", *args, **kwargs)
