from spm.__wrap__ import _Runtime


def _denoise_artifact(*args, **kwargs):
  """  DENOISE_ARTIFACT can be used for denoising source separation (DSS)  
    during component analysis  
     
    See also COMPONENTANALYSIS  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/denoise_artifact.m)
  """

  return _Runtime.call("denoise_artifact", *args, **kwargs)
