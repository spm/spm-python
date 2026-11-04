from spm._runtime import Runtime


def _read_neuromag_maxfilterlog(*args, **kwargs):
    r"""
      READ_NEUROMAG_MAXFILTERLOG reads the ascii logfile that is produced by MaxFilter  
         
        Use as  
         log = read_neuromag_maxfilterlog(filename)  
         
        See also READ_NEUROMAG_EVE, READ_NEUROMAG_HC  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_neuromag_maxfilterlog.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_neuromag_maxfilterlog", *args, **kwargs)
