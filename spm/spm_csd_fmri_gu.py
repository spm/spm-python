from spm.__wrapper__ import Runtime


def spm_csd_fmri_gu(*args, **kwargs):
  """  Spectra of neuronal fluctuations and noise  
    FORMAT [Gu,Gn,Hz,dt] = spm_csd_fmri_gu(P,dt)  
     
    P  - model parameters  
    dt - sampling interval  
     
    This routine returns the spectra of neuronal fluctuations and noise for a  
    standard frequency range specified by the sampling interval.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_csd_fmri_gu.m)
  """

  return Runtime.call("spm_csd_fmri_gu", *args, **kwargs)
