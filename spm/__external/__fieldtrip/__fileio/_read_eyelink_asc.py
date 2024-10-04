from spm.__wrap__ import _Runtime


def _read_eyelink_asc(*args, **kwargs):
  """  READ_EYELINK_ASC reads the header information, input triggers, messages  
    and all data points from an Eyelink *.asc file. The output events are  
    represented as matlab tables (after Aug 2022)  
     
    Use as  
      asc = read_eyelink_asc(filename)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_eyelink_asc.m)
  """

  return _Runtime.call("read_eyelink_asc", *args, **kwargs)
