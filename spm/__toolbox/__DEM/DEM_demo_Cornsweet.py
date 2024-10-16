from spm.__wrapper__ import Runtime


def DEM_demo_Cornsweet(*args, **kwargs):
  """  The Cornsweet effect: This demo illustrates the inference underlying the  
    Cornsweet effect or illusion. It exploits formal priors on the spatial  
    contiguity of the illuminant and reflectance; where the illuminant does not  
    have edges, but the reflectance can. This is implemented using a  
    discrete cosine set (DCT) as the spatial basis for the illuminant and a   
    (Haar) Discrete Wavelet transform (DWT) for the reflectance. Appropriate  
    shrinkage priors on the (implicit) transform coefficients ensure that the  
    explanation for visual input (reflectance times illuminant) assigns edges  
    to the reflectance; thereby producing the Cornsweet effect.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_demo_Cornsweet.m)
  """

  return Runtime.call("DEM_demo_Cornsweet", *args, **kwargs, nargout=0)
