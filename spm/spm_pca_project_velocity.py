from spm.__wrapper__ import Runtime


def spm_pca_project_velocity(*args, **kwargs):
  """  FORMAT z = project_velocity(v, [fmodel], [fsubspace])  
      v           - [Nx Ny Nz 3] Initial velocity  
      fmodel    - Path to the model parameters {'model/model_variables.mat'}  
      fsubspace - Path to the scaled subspace {'model/subspace_scaled.nii'}  
      z         - [M 1] Latent code  
    Yael Balabastre 2024  
    -------------------------------------------------------------------------  
    Path to model file  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_pca_project_velocity.m)
  """

  return Runtime.call("spm_pac_project_velocity", *args, **kwargs)
