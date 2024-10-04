from spm.__wrap__ import _Runtime


def spm_deformations(*args, **kwargs):
  """  Various deformation field utilities  
    FORMAT out = spm_deformations(job)  
    job - a job created via spm_cfg_deformations.m  
    out - a struct with fields  
          .def    - file name of created deformation field  
          .warped - file names of warped images  
     
    See spm_cfg_deformations.m for more information.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_deformations.m)
  """

  return _Runtime.call("spm_deformations", *args, **kwargs)
