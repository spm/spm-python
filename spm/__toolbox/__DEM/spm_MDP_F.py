from spm.__wrap__ import _Runtime


def spm_MDP_F(*args, **kwargs):
  """  auxiliary function for retrieving free energy and its components  
    FORMAT [F,Fu,Fs,Fq,Fg,Fa] = spm_MDP_F(MDP)  
     
    F   - total free energy  
    Fu  - confidence  
    Fs  - free energy of states  
    Fq  - free energy of policies  
    Fg  - free energy of precision  
    Fa  - free energy of parameters  
     
    If MDP is a cell array, the free actions are turned (summed over time),  
    otherwise, the free energies are turned over time  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/spm_MDP_F.m)
  """

  return _Runtime.call("spm_MDP_F", *args, **kwargs)
