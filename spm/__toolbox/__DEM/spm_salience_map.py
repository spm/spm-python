from spm.__wrap__ import _Runtime


def spm_salience_map(*args, **kwargs):
  """  creates a salience map  
    FORMAT [S L] = spm_salience_map(M,n)  
     
    S  - Salience (n x n,1)  
    L  - list of (fictive) hidden control states (range of S)  
     
    M  - generative model (with M(2).v and M(1).xo encoding location (L)  
    n  - dimension of map (S)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/spm_salience_map.m)
  """

  return _Runtime.call("spm_salience_map", *args, **kwargs)
