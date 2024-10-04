from spm.__wrap__ import _Runtime


def spm_shoot_divergence(*args, **kwargs):
  """  Compute divergences from velocity fields  
    FORMAT spm_shoot_divergence(job)  
    job.velocities - Filenames of initial velocity fields  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/Shoot/spm_shoot_divergence.m)
  """

  return _Runtime.call("spm_shoot_divergence", *args, **kwargs)
