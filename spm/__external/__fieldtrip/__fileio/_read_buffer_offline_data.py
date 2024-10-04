from spm.__wrap__ import _Runtime


def _read_buffer_offline_data(*args, **kwargs):
  """  function dat = read_buffer_offline_data(datafile, header, range)  
     
    This function reads FCDC buffer-type data from a binary file.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_buffer_offline_data.m)
  """

  return _Runtime.call("read_buffer_offline_data", *args, **kwargs)
