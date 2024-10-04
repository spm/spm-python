from spm.__wrap__ import _Runtime


def _read_asa_dip(*args, **kwargs):
  """  READ_ASA_DIP reads the dipole position, moment and amplitude  
    This importer is designed for fixed-dipole models and only supports   
    a limited number of the options that ASA has.  
     
    Use as  
      [pos, mom, ampl, time] = read_asa_dip(filename)  
     
    See also READ_ASA_VOL, READ_ASA_MRI  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_asa_dip.m)
  """

  return _Runtime.call("read_asa_dip", *args, **kwargs)
