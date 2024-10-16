from spm.__wrapper__ import Runtime


def spm_cost_SHC_path(*args, **kwargs):
  """  plots path for cost_SHC demo's  
    FORMAT spm_cost_SHC_path(qU,A)  
     
    qU  - DEM condotioal esimates of states  
    A.x - locations of attrcuor  
    A.d - radius  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/spm_cost_SHC_path.m)
  """

  return Runtime.call("spm_cost_SHC_path", *args, **kwargs, nargout=0)
