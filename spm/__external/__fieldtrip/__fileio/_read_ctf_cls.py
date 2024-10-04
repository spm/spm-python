from spm.__wrap__ import _Runtime


def _read_ctf_cls(*args, **kwargs):
  """  READ_CTF_CLS reads the classification file from a CTF dataset  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_ctf_cls.m)
  """

  return _Runtime.call("read_ctf_cls", *args, **kwargs)
