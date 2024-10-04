from spm.__wrap__ import _Runtime


def spm_load_priors8(*args, **kwargs):
  """  Load the tissue probability maps for segmentation  
    FORMAT tpm = spm_load_priors8(V)  
    V   - structures of image volume information (or filenames)  
    tpm - a structure for tissue probabilities  
     
    This function is intended to be used in conjunction with spm_sample_priors.  
    V = spm_vol(P);  
    T = spm_load_priors(V);  
    B = spm_sample_priors(T,X,Y,Z);  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_load_priors8.m)
  """

  return _Runtime.call("spm_load_priors8", *args, **kwargs)
