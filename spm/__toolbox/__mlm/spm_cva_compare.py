from spm.__wrap__ import _Runtime


def spm_cva_compare(*args, **kwargs):
  """  Model comparison for probabilistic CVA  
    FORMAT [CVA] = spm_cva_compare (Y,X,c)  
     
    Y  [N x d1] data matrix  
    X  [N x d2] design matrix  
    c  Contrast vector (if specified)  
     
    CVA has fields:  
     
    .order        number of canonical vectors (latent space dimension)  
    .bic          BIC for each order  
    .aic          AIC for each order  
     
    and   
     
    .U1,.U2      Canonical vectors  
    .W1,.W2      Factor matrices  
     
    for the highest order model.  
     
    See spm_cva_prob.m for more details  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mlm/spm_cva_compare.m)
  """

  return _Runtime.call("spm_cva_compare", *args, **kwargs)
