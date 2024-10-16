from spm.__wrapper__ import Runtime


def _read_mff_bin(*args, **kwargs):
  """  READ_MFF_BIN  
     
    Use as  
      [hdr] = read_mff_bin(filename)  
    or  
      [dat] = read_mff_bin(filename, begblock, endblock);  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_mff_bin.m)
  """

  return Runtime.call("read_mff_bin", *args, **kwargs)
