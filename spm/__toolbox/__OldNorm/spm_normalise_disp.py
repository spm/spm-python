from spm.__wrap__ import _Runtime


def spm_normalise_disp(*args, **kwargs):
  """  Display results of spatial normalisation  
    FORMAT spm_normalise_disp(matname)  
    matname - name of parameter file *_sn.mat  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/OldNorm/spm_normalise_disp.m)
  """

  return _Runtime.call("spm_normalise_disp", *args, **kwargs, nargout=0)
