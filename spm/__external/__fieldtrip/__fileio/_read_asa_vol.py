from spm.__wrap__ import _Runtime


def _read_asa_vol(*args, **kwargs):
  """  READ_ASA_VOL reads an ASA volume conductor file  
     
    all data is converted to the following units  
      vertices        mm  
      conductivities  S/m  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_asa_vol.m)
  """

  return _Runtime.call("read_asa_vol", *args, **kwargs)
