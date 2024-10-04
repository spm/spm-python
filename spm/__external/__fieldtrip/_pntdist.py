from spm.__wrap__ import _Runtime


def _pntdist(*args, **kwargs):
  """  PNTDIST returns the euclidian distance between two points  
     
     [dist] = pntdist(pnt1, pnt2)  
     
    where pnt1 and pnt2 must be Npnt x 3  
    or either one can be Npnt x 1  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/pntdist.m)
  """

  return _Runtime.call("pntdist", *args, **kwargs)
