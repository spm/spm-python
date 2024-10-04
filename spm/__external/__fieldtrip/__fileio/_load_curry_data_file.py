from spm.__wrap__ import _Runtime


def _load_curry_data_file(*args, **kwargs):
  """load_curry_data_file is a function.  
      [orig, data] = load_curry_data_file(datafile)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/load_curry_data_file.m)
  """

  return _Runtime.call("load_curry_data_file", *args, **kwargs)
