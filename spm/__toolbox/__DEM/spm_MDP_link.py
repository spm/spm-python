from spm.__wrapper__ import Runtime


def spm_MDP_link(*args, **kwargs):
  """  auxiliary function to create link (cell array)  
    FORMAT [LINK,link] = spm_MDP_link(MDP)  
     
    MDP.MDP  - hierarchical MDP structure  
     
    LINK  - cell array of (binary) matrices linking outputs to states  
    link  - (binary) matrix of non-empty links  
     
    this routine assumes unique names in MDP.labels  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/spm_MDP_link.m)
  """

  return Runtime.call("spm_MDP_link", *args, **kwargs)
