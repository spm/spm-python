from spm.__wrapper__ import Runtime


def _denoise_artifact(*args, **kwargs):
  """  DENOISE_ARTIFACT can be used for denoising source separation (DSS)  
    during component analysis  
     
    See also COMPONENTANALYSIS  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/denoise_artifact.m)
  """

  return Runtime.call("denoise_artifact", *args, **kwargs)
