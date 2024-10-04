from spm.__wrap__ import _Runtime


def spm_dcm_fmri_csd_gen(*args, **kwargs):
  """  Conversion routine for DEM inversion of DCM for CSD (fMRI)  
    FORMAT y = spm_dcm_fmri_csd_gen(x,v,P)  
     
    This routine computes the spectral response of a network of regions  
    driven by  endogenous fluctuations and exogenous (experimental) inputs.  
    It returns the complex cross spectra of regional responses as a  
    three-dimensional array. The endogenous innovations or fluctuations are  
    parameterised in terms of a (scale free) power law, in frequency space.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_dcm_fmri_csd_gen.m)
  """

  return _Runtime.call("spm_dcm_fmri_csd_gen", *args, **kwargs)
