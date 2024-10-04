from spm.__wrap__ import _Runtime


def _read_ctf_shape(*args, **kwargs):
  """  READ_CTF_SHAPE reads headshape points and header information  
    from a CTF *.shape the accompanying *.shape_info file.  
     
    Use as  
      [shape] = read_ctf_shape(filename)  
    where filename should have the .shape extension  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_ctf_shape.m)
  """

  return _Runtime.call("read_ctf_shape", *args, **kwargs)
