from spm.__wrapper__ import Runtime


def spm_normalise_disp(*args, **kwargs):
  """  Display results of spatial normalisation  
    FORMAT spm_normalise_disp(matname)  
    matname - name of parameter file *_sn.mat  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/OldNorm/spm_normalise_disp.m)
  """

  return Runtime.call("spm_normalise_disp", *args, **kwargs, nargout=0)
