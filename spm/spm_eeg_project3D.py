from spm.__wrapper__ import Runtime


def spm_eeg_project3D(*args, **kwargs):
  """  Wrapper function to a fieldtrip function to project 3D locations   
    onto a 2D plane.   
    FORMAT [xy,label] = spm_eeg_project3D(sens, modality)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_eeg_project3D.m)
  """

  return Runtime.call("spm_eeg_project3D", *args, **kwargs)
