from spm.__wrap__ import _Runtime


def spm_MDP_L(*args, **kwargs):
  """  log-likelihood function  
    FORMAT L = spm_mdp_L(P,M,U,Y)  
    P    - parameter structure  
    M    - generative model  
    U    - inputs (observations or stimuli)  
    Y    - observed responses (or choices)  
     
    This auxiliary function evaluates the log likelihood of a sequence of  
    choices within and between trials under and MDP model of choice behaviour  
    parameterised by P.required fields of the model MR:  
     
    M.G   - a function that returns a particular MDP parameterisation; i.e.,  
            MDP = M.G(P);  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/spm_MDP_L.m)
  """

  return _Runtime.call("spm_MDP_L", *args, **kwargs)
