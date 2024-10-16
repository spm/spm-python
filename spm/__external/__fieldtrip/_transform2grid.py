from spm.__wrapper__ import Runtime


def _transform2grid(*args, **kwargs):
  """  TRANSFORM2GRID ensures that the volume contains the definition of the  
    cardian axes, i.e. xgrid/ygrid/zgrid. If the voluyme contains a  
    homogenous coordinate transformation axis that is unequal to eye(4), it  
    will try to construct the cardinal axis from that transformation matrix.  
     
    See also GRID2TRANSFORM  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/transform2grid.m)
  """

  return Runtime.call("transform2grid", *args, **kwargs)
