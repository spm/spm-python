from spm.__wrap__ import _Runtime


def _read_deymed_ini(*args, **kwargs):
  """  READ_DEYMED_INI reads EEG data from the Deymed Truescan file format  
     
    Use as  
      hdr = read_deymed_ini(filename)  
     
    See also READ_DEYMED_DAT  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_deymed_ini.m)
  """

  return _Runtime.call("read_deymed_ini", *args, **kwargs)
