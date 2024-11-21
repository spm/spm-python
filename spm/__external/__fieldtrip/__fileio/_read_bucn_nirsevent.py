from spm.__wrapper__ import Runtime


def _read_bucn_nirsevent(*args, **kwargs):
    """
      READ_BUCN_NIRSEVENT reads the event information of ASCII-formatted NIRS   
        data acquired with the UCL-BIRKBECK machine and postprocessed by the  
        Paris group. The first line contains the header-info and the rest of  
        the file contains per line an event. The first column specifies the  
        time of the event in samples, the second column specifies the time of the  
        event in seconds, the third column contains the event type and the fourth  
        column is the event value.  
         
        Use as  
          [event] = read_bucn_nirshdr(filename)  
         
        See also READ_BUCN_NIRSHDR, READ_BUCN_NIRSDATA  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_bucn_nirsevent.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_bucn_nirsevent", *args, **kwargs)
