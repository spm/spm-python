from spm.__wrap__ import _Runtime


def routlm(*args, **kwargs):
  """  ROUTLM computes the projection of a point from its la/mu parameters  
    these equal the "Barycentric" coordinates  
     
    Use as  
      [proj] = routlm(v1, v2, v3, la, mu)  
    where v1, v2 and v3 are three vertices of the triangle  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/src/routlm.m)
  """

  return _Runtime.call("routlm", *args, **kwargs)
