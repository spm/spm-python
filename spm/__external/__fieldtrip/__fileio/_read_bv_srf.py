from spm.__wrap__ import _Runtime


def _read_bv_srf(*args, **kwargs):
  """  READ_BV_SRF reads a triangulated surface from a BrainVoyager *.srf file  
     
    Use as  
      [pnt, tri] = read_bv_srf(filename) or  
      [pnt, tri, srf] = read_bv_srf(filename)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_bv_srf.m)
  """

  return _Runtime.call("read_bv_srf", *args, **kwargs)
