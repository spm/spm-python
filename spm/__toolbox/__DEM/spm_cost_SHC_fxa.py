from spm.__wrap__ import _Runtime


def spm_cost_SHC_fxa(*args, **kwargs):
  """  equations of motion for a foraging problem  
    FORMAT [f] = spm_cost_SHC_fxa(x,v,a,P)  
     
    x   - hidden states  
    v   - exogenous inputs  
    a   - action  
    P   - parameters for mountain car  
     
    returns f = dx/dt (see spm_cost_SHC_fx)  
    These equations of motion model dissipative flow x.x and x.v on a flat   
    potential and increases in physiological states x.q as radial basis   
    functions of secrete locations. The agent has to discover these   
    locations % using an appropriate policy. This generative process would   
    also substitute for Morris water-maze simulations or unbounded saccades.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/spm_cost_SHC_fxa.m)
  """

  return _Runtime.call("spm_cost_SHC_fxa", *args, **kwargs)
