from spm.__wrap__ import _Runtime


def spm_shoot_warp(*args, **kwargs):
  """  Register images with template  
    format spm_shoot_warp(job)  
    Fields of job:  
        job.images{1} first set of images (eg rc1*.nii)  
        job.images{2} second set of images (eg rc2*.nii)  
        etc  
        job.templates template files  
    Other settings are defined in spm_shoot_defaults.m  
     
    The outputs are flow fields (v*.nii), deformation fields (y*.nii) and  
    Jacobian determinants (j*.nii)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/Shoot/spm_shoot_warp.m)
  """

  return _Runtime.call("spm_shoot_warp", *args, **kwargs)
