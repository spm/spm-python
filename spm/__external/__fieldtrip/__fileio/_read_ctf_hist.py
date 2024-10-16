from spm.__wrapper__ import Runtime


def _read_ctf_hist(*args, **kwargs):
  """  READ_CTF_HIST  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_ctf_hist.m)
  """

  return Runtime.call("read_ctf_hist", *args, **kwargs)
