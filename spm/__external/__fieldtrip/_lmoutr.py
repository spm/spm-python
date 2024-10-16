from spm.__wrapper__ import Runtime


def _lmoutr(*args, **kwargs):
  """  LMOUTR computes the la/mu parameters of a point projected to a triangle  
     
    Use as  
      [la, mu, dist] = lmoutr(v1, v2, v3, r)  
    where v1, v2 and v3 are three vertices of the triangle, and r is   
    the point that is projected onto the plane spanned by the vertices  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/lmoutr.m)
  """

  return Runtime.call("lmoutr", *args, **kwargs)
