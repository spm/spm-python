from spm.__wrap__ import _Runtime


def _read_ctf_hdm(*args, **kwargs):
  """  READ_CTF_HDM reads the head volume conductor model from a *.hdm file  
     
    vol = read_ctf_hdm(filename)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_ctf_hdm.m)
  """

  return _Runtime.call("read_ctf_hdm", *args, **kwargs)
