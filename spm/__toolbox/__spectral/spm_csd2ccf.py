from spm.__wrap__ import _Runtime


def spm_csd2ccf(*args, **kwargs):
  """  Converts cross spectral density to cross covariance function  
    FORMAT [ccf,pst] = spm_csd2ccf(csd,Hz,dt)  
     
    csd  (n,:,:)          - cross spectral density (cf, mar.P)  
    Hz   (n x 1)          - vector of frequencies (Hz)  
    dt                    - samping interval [default = 1/(2*Hz(end))]  
     
    ccf                   - cross covariance functions  
    pst  (N,1)            - vector of lags for evaluation (seconds)  
     
    Note that because this scheme uses FFT one can only change dt.  
     
    See also:   
     spm_ccf2csd.m, spm_ccf2mar, spm_csd2ccf.m, spm_csd2mar.m, spm_mar2csd.m,  
     spm_csd2coh.m, spm_Q.m, spm_mar.m and spm_mar_spectral.m  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/spectral/spm_csd2ccf.m)
  """

  return _Runtime.call("spm_csd2ccf", *args, **kwargs)
