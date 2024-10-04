from spm.__wrap__ import _Runtime


def DEM_demo_Gabor(*args, **kwargs):
  """  State-space demo routine simulating position invariant representations  
    in the visual system.  The generative model predicts a one-dimensional  
    Gabor patch that moves in a (one-dimensional) visual field. The  
    inversion of this dynamic model can be viewed as deconvolving spatial and  
    category attributes from a moving stimulus (or selective re-sampling of  
    the input) to recover the stimulus that can be represented. The  
    prediction shown in the lower panels had position information removed.  
   ___________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_demo_Gabor.m)
  """

  return _Runtime.call("DEM_demo_Gabor", *args, **kwargs, nargout=0)
