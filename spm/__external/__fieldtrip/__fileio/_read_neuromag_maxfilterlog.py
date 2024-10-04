from spm.__wrap__ import _Runtime


def _read_neuromag_maxfilterlog(*args, **kwargs):
  """  READ_NEUROMAG_MAXFILTERLOG reads the ascii logfile that is produced by MaxFilter  
     
    Use as  
     log = read_neuromag_maxfilterlog(filename)  
     
    See also READ_NEUROMAG_EVE, READ_NEUROMAG_HC  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_neuromag_maxfilterlog.m)
  """

  return _Runtime.call("read_neuromag_maxfilterlog", *args, **kwargs)
