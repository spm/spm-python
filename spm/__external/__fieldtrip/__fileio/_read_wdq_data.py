from spm.__wrapper__ import Runtime


def _read_wdq_data(*args, **kwargs):
  """  READ_WDQ_DATA reads data from wdq files  
     
    Use as  
     [dat] = read_wdq_data(filename, hdr, begsample, endsample, chanindx)  
    or  
     [dat] = read_wdq_data(filename, hdr, 'lowbits')  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_wdq_data.m)
  """

  return Runtime.call("read_wdq_data", *args, **kwargs)
