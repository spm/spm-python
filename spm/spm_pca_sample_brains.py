from spm.__wrapper__ import Runtime


def spm_pca_sample_brains(*args, **kwargs):
  """  FORMAT  spm_pca_sample_brains(Nb, PC, sp, output_folder, template_folder,template_meshfiles,randseed)  
      Nb - Number of brains to make  
      PC- vector of indices principal components to use eg [8:100]  
    some PC indices can be negative meaning their pca components (2) will be linearly shifted in opposite direction  
    i.e. [1 2] and [1 -2] are two different trajectories where 2nd component moves in opposite direction  
      sp- span in terms of z eg 3 gives range z=-3 -> +3  
      output_folder - Folder where to write generated gifti files {'.'}  
      template_folder- folder where the template brain principalc components  
      are stored   
    template_mesh_files- optional- defaults to cortex, but could also supply  
    inner-skull mesh to be deformed etc  
    rand_seed- optional unique file identifier (eg for different distortion  
    trajectories)  
    Jose David Lopez, Yael Balbastre, Gareth Barnes 2024  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_pca_sample_brains.m)
  """

  return Runtime.call("spm_pca_sample_brains", *args, **kwargs)
