from spm.__wrapper__ import Runtime


def spm_ccf2csd(*args, **kwargs):
  """  Converts cross covariance function to cross spectral density  
    FORMAT [csd,Hz] = spm_ccf2csd(ccf,Hz)  
     
    ccf  (N,:,:)          - cross covariance functions  
    Hz   (n x 1)          - vector of frequencies (Hz)  
     
    csd  (n,:,:)          - cross spectral density (cf, mar.P)  
     
    See also: spm_???2???.m  
        ??? = {'ccf','csd','gew','mar','coh','mtf','ker','ssm','dcm'}  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/spectral/spm_ccf2csd.m)
  """

  return Runtime.call("spm_ccf2csd", *args, **kwargs)
