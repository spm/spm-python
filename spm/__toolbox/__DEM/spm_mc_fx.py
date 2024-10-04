from spm.__wrap__ import _Runtime


def spm_mc_fx(*args, **kwargs):
  """  equations of motion for the mountain car problem using basis functions  
    problem  
    FORMAT [f] = spm_mc_fx(x,v,P)  
     
    x     - hidden states  
    v     - exogenous inputs  
    P.x,k - parameters for gradient function:     G(x(1),P.p)  
    P.q   - parameters for cost or loss-function: C(x(1),P.q)  
     
    returns f = dx/dt = f  = [x(2);  
                              G - x(2)*C(x(1))]*dt;  
     
    where C determines divergence of flow x(2) at any position x(1).  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/spm_mc_fx.m)
  """

  return _Runtime.call("spm_mc_fx", *args, **kwargs)
