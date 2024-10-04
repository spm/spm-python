from spm.__wrap__ import _Runtime


def _read_deymed_dat(*args, **kwargs):
  """  READ_DEYMED_DAT reads EEG data from the Deymed Truescan file format  
     
    Use as  
      dat = read_deymed_dat(filename, hdr, begsample, endsample)  
     
    See also READ_DEYMED_INI  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_deymed_dat.m)
  """

  return _Runtime.call("read_deymed_dat", *args, **kwargs)
