from spm.__wrap__ import _Runtime


def _read_elec(*args, **kwargs):
  """  READ_ELEC reads "la/mu" electrode parameters from a MBF electrode file  
    which are used to position them on a triangulated surface  
     
    [el, lab] = read_elec(filename)  
     
    where el = [tri, la, mu]  
    and lab contains the electrode labels (if present)  
     
    See also READ_TRI, TRANSFER_ELEC  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_elec.m)
  """

  return _Runtime.call("read_elec", *args, **kwargs)
