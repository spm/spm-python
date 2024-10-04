from spm.__wrap__ import _Runtime


def spm_DEM_basis(*args, **kwargs):
  """  evaluates a parameterized set of basis functions  
    problem  
    FORMAT [f,p] = spm_DEM_basis(x,v,P)  
     
    x   - hidden states  
    v   - causal inputs  
    P   - parameters  
     
    f   - f(x)  
    p   - p(i)  
     
    returns:  
      f = sum(P(i)*B(x,i))  
      P = p/sum(p)  
     
    where B(x,i) are basis functions  
     
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/spm_DEM_basis.m)
  """

  return _Runtime.call("spm_DEM_basis", *args, **kwargs)
