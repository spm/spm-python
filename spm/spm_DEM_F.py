from spm.__wrapper__ import Runtime


def spm_DEM_F(*args, **kwargs):
  """  Free-energy as a function of conditional parameters  
    FORMAT [F,p] = spm_DEM_F(DEM,ip)  
     
    DEM    - hierarchical model  
     
    F(i)   - free-energy at <q(P(ip))> = p(i)  
     
    where p(i) is the ip-th free-parameter. This is a bound on   
    the log-likehood (log-evidence) conditioned on the expected parameters.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_DEM_F.m)
  """

  return Runtime.call("spm_DEM_F", *args, **kwargs)
