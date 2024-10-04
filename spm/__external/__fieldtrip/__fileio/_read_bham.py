from spm.__wrap__ import _Runtime


def _read_bham(*args, **kwargs):
  """  READ_BHAM reads the EEG data files as recorded by Praamstra in Birmingham  
    the datafiles are in a particular ascii format  
     
    [dat, lab] = read_bham(filename)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_bham.m)
  """

  return _Runtime.call("read_bham", *args, **kwargs)
