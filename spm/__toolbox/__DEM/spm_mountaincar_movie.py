from spm.__wrap__ import _Runtime


def spm_mountaincar_movie(*args, **kwargs):
  """  makes a move for mountain car problem  
    FORMAT spm_mountaincar_movie(DEM)  
     
    see:  
    Gaussian Processes in Reinforcement Learning  
    Carl Edward Rasmussen and Malte Kuss  
    Max Planck Institute for Biological Cybernetics  
    Spemannstraße 38, 72076 T¨ubingen, Germany  
    {carl,malte.kuss}@tuebingen.mpg.de  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/spm_mountaincar_movie.m)
  """

  return _Runtime.call("spm_mountaincar_movie", *args, **kwargs, nargout=0)
