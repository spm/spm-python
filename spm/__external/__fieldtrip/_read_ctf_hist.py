from spm.__wrap__ import _Runtime


def _read_ctf_hist(*args, **kwargs):
  """  READ_CTF_HIST  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/read_ctf_hist.m)
  """

  return _Runtime.call("read_ctf_hist", *args, **kwargs)
