from spm.__wrap__ import _Runtime


def _read_ctf_mri(*args, **kwargs):
  """  READ_CTF_MRI reads header and image data from a CTF version 2.2 MRI file  
     
    Use as  
      [mri, hdr] = read_ctf_mri(filename)  
     
    See also READ_CTF_MRI4  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_ctf_mri.m)
  """

  return _Runtime.call("read_ctf_mri", *args, **kwargs)
