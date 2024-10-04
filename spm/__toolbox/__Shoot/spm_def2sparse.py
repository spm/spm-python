from spm.__wrap__ import _Runtime


def spm_def2sparse(*args, **kwargs):
  """  Generate a sparse matrix encoding a deformation  
    [Phi,dim1,dim2] = spm_def2sparse(PY,PI)  
    PY - Filename of deformation field  
    PI - Filename of image defining field of view etc  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/Shoot/spm_def2sparse.m)
  """

  return _Runtime.call("spm_def2sparse", *args, **kwargs)
