from spm.__wrapper__ import Runtime


def _read_tdt_tsq(*args, **kwargs):
  """  READ_TDT_TSQ reads the headers from a Tucker_Davis_technologies TSQ file  
     
    tsq file is a heap of event headers, which is ?40 byte each,  
    ordered strictly by time  
     
    Use as  
      tsq = read_tdt_tsq(filename, begblock, endblock)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_tdt_tsq.m)
  """

  return Runtime.call("read_tdt_tsq", *args, **kwargs)
