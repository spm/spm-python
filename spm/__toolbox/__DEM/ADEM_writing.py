from spm.__wrap__ import _Runtime


def ADEM_writing(*args, **kwargs):
  """  This demo illustrates how action can fulfill prior expectations by   
    explaining away sensory prediction errors prescribed by desired movement   
    trajectories. In this example a two-joint arm follows a stable   
    heteroclinic channel, prescribed by a set of fixed point attractors. The   
    locations of the successive (autovitiated) attractors are defined by   
    parameters. The ensuing trajectories are illustrated here in terms of   
    synthetic writing.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/ADEM_writing.m)
  """

  return _Runtime.call("ADEM_writing", *args, **kwargs, nargout=0)
