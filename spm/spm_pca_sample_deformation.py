from spm.__wrapper__ import Runtime


def spm_pca_sample_deformation(*args, **kwargs):
  """  FORMAT [iy,y] = sample_deformation([z0], [fname])  
      z0 - [M 1] Latent code. NaN values will be sampled from the  
           distribution {default: NaN}  
      fname - Path to the scaled subspace fail {'model/subspace_scaled.nii'}  
      iy - [Nx Ny Nz 3] Inverse deformation (used to forward deform meshes)  
      y  - [Nx Ny Nz 3] Forward deformation (used to forward deform volumes)  
      z  - [M 1] Sampled latent code  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_pca_sample_deformation.m)
  """

  return Runtime.call("spm_pac_sample_deformation", *args, **kwargs)
