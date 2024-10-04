from spm.__wrap__ import _Runtime


def ADEM_reaching(*args, **kwargs):
  """  This demo illustrates how action can fulfil prior expectations by  
    explaining away sensory prediction errors prescribed by desired movement  
    trajectories. In this example a two-joint arm is trained to touch a target  
    so that spontaneous reaching occurs after training.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/ADEM_reaching.m)
  """

  return _Runtime.call("ADEM_reaching", *args, **kwargs, nargout=0)
