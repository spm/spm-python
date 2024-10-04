from spm.__wrap__ import _Runtime


def spm_MDP_DP(*args, **kwargs):
  """  dynamic programming using active inference  
    FORMAT [B0,BV] = spm_MDP_DP(MDP)  
     
    MDP.A(O,N)      - Likelihood of O outcomes given N hidden states  
    MDP.B{M}(N,N)   - transition probabilities among hidden states (priors)  
    MDP.C(N,1)      - prior preferences (prior over future states)  
     
    MDP.V(T - 1,P)  - P allowable policies (control sequences)  
     
    B0      - optimal state action policy or transition matrix  
    BV      - corresponding policy using value iteration  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/spm_MDP_DP.m)
  """

  return _Runtime.call("spm_MDP_DP", *args, **kwargs)
