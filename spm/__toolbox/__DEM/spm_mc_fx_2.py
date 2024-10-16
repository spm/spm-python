from spm.__wrapper__ import Runtime


def spm_mc_fx_2(*args, **kwargs):
  """  equations of motion for the mountain car problem using basis functions  
    problem  
    FORMAT [f] = spm_mc_fx_2(x,v,P)  
     
    x   - hidden states  
    v   - exogenous inputs  
    P.p - parameters for gradient function:     G(x(1),P.p)  
    P.q - parameters for cost or loss function: C(x(1),P.q)  
     
    returns f = dx/dt = f  = [x(2);  
                              G - x(2)*C]*dt;  
     
    where C determines divergence of flow x(2) at any position x(1).  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/spm_mc_fx_2.m)
  """

  return Runtime.call("spm_mc_fx_2", *args, **kwargs)
