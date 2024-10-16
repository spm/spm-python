from spm.__wrapper__ import Runtime


def spm_pca_get_transforms(*args, **kwargs):
  """  z are latent vectors describing the space in which the MRI lives : vector of 100 elements  
    also get a copy of nativeMRI in template space in output_folder (optional)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_pca_get_transforms.m)
  """

  return Runtime.call("spm_pca_get_transforms", *args, **kwargs)
