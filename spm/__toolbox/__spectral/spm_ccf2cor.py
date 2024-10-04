from spm.__wrap__ import _Runtime


def spm_ccf2cor(*args, **kwargs):
  """  Converts  cross covariance function to correlation and covariance  
    FORMAT [cor,cov] = spm_ccf2cor(ccf)  
     
    ccf  (N,n,n) - cross covariance function  
     
    cor  (n,n)   - correlation  
    cov  (n,n)   - covariance  
     
    See also:   
     spm_ccf2csd.m, spm_ccf2mar, spm_csd2ccf.m, spm_csd2mar.m, spm_mar2csd.m,  
     spm_csd2coh.m, spm_Q.m, spm_mar.m and spm_mar_spectral.m  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/spectral/spm_ccf2cor.m)
  """

  return _Runtime.call("spm_ccf2cor", *args, **kwargs)
