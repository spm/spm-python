from spm.__wrapper__ import Runtime


def _read_neuromag_maxfilterlog(*args, **kwargs):
    """
      READ_NEUROMAG_MAXFILTERLOG reads the ascii logfile that is produced by MaxFilter  
         
        Use as  
         log = read_neuromag_maxfilterlog(filename)  
         
        See also READ_NEUROMAG_EVE, READ_NEUROMAG_HC  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_neuromag_maxfilterlog.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_neuromag_maxfilterlog", *args, **kwargs)
