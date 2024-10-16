from spm.__wrapper__ import Runtime


def spm_MDP_da(*args, **kwargs):
  """  Simulated histograms of dopamine firing  
    FORMAT spm_MDP_da(MDP)  
     
    See also: spm_MDP_game, which generalises this scheme and replaces prior  
    beliefs about KL control with minimisation of expected free energy.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_MDP_da.m)
  """

  return Runtime.call("spm_MDP_da", *args, **kwargs, nargout=0)
