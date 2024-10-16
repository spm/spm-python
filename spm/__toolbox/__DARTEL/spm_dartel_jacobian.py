from spm.__wrapper__ import Runtime


def spm_dartel_jacobian(*args, **kwargs):
  """  Generate Jacobian determinant fields  
    FORMAT spm_dartel_jacobian(job)  
    job.flowfields - Filenames of flowfields  
    job.K          - 2^K timesteps are used  
     
    Note that K needs to be reasonably large in order to obtain reasonable  
    Jacobian determinant fields.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DARTEL/spm_dartel_jacobian.m)
  """

  return Runtime.call("spm_dartel_jacobian", *args, **kwargs)
