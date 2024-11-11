from spm.__wrapper__ import Runtime


def _read_tdt_tsq(*args, **kwargs):
    """
      READ_TDT_TSQ reads the headers from a Tucker_Davis_technologies TSQ file  
         
        tsq file is a heap of event headers, which is ?40 byte each,  
        ordered strictly by time  
         
        Use as  
          tsq = read_tdt_tsq(filename, begblock, endblock)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_tdt_tsq.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_tdt_tsq", *args, **kwargs)
