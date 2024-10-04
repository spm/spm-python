from spm.__wrap__ import _Runtime


def spm_vpca_f(*args, **kwargs):
  """  Compute free energy of VPCA model  
    FORMAT [Fm] = spm_vpca_f (pca,c)  
     
    pca   data structure (see eg. spm_vpca.m)  
    c     information about single component  
     
    Fm    negative free energy of model  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mlm/spm_vpca_f.m)
  """

  return _Runtime.call("spm_vpca_f", *args, **kwargs)
