from spm.__wrapper__ import Runtime


def spm_cost_fxa(*args, **kwargs):
  """  equations of motion for a foraging problem  
    problem  
    FORMAT [f] = spm_cost_fxa(x,v,a,P)  
     
    x   - hidden states  
    v   - exogenous inputs  
    a   - action  
    P   - parameters for mountain car  
     
    returns f = dx/dt   
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/spm_cost_fxa.m)
  """

  return Runtime.call("spm_cost_fxa", *args, **kwargs)
