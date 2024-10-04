from spm.__wrap__ import _Runtime


def spm_eeg_smoothmesh_mm(*args, **kwargs):
  """  Compute smoothing kernel for triangle mesh in mm  
    FORMAT [allsmoothnames] = spm_eeg_smoothmesh_mm(meshname,allfwhm,redo)  
     
    smoothing kernel: each colum QG(:,j)  
    if redo==1 and file already exists then redo  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_eeg_smoothmesh_mm.m)
  """

  return _Runtime.call("spm_eeg_smoothmesh_mm", *args, **kwargs)
