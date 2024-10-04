from spm.__wrap__ import _Runtime


def spm_lotka_volterra(*args, **kwargs):
  """  Equations of motion for Lotka-Volterra dynamics  
    FORMAT [f] = spm_lotka_volterra(x,v,P)  
    FORMAT [f] = spm_lotka_volterra(x,v)  
    FORMAT [P] = spm_lotka_volterra(n)  
     
    x     - hidden states  
    v     - parameter of P.f  
    P     - lateral connectivity  
     
    returns f = dx/dt = P*S(x) - x/8 + 1;  
                 S(x) = 1./(1 + exp(-x))  
     
    where P determines the order of unstable fixed points visited in the  
    stable heteroclinic channel. If P is not specified it will be computed  
    using v. If x is a scalar a matrix of size x (P) is returned (with v = 1).  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_lotka_volterra.m)
  """

  return _Runtime.call("spm_lotka_volterra", *args, **kwargs)
