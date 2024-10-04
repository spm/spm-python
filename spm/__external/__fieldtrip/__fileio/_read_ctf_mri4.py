from spm.__wrap__ import _Runtime


def _read_ctf_mri4(*args, **kwargs):
  """  READ_CTF_MRI reads header and imnage data from CTF format MRI file  
     
    [mri, hdr] = read_ctf_mri(filename)  
     
    See also READ_CTF_MEG4, READ_CTF_RES4  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_ctf_mri4.m)
  """

  return _Runtime.call("read_ctf_mri4", *args, **kwargs)
