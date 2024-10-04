from spm.__wrap__ import _Runtime


def _read_ctf_res4(*args, **kwargs):
  """  READ_CTF_RES4 reads the header in RES4 format from a CTF dataset  
     
    Use as  
      [hdr] = read_ctf_res4(filename)  
     
    See also READ_CTF_MEG4  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_ctf_res4.m)
  """

  return _Runtime.call("read_ctf_res4", *args, **kwargs)
