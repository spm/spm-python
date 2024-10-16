from spm.__wrapper__ import Runtime


def bf_inverse_minimumnorm(*args, **kwargs):
  """  Computes Minimum Norm projectors  
     
    Please cite:  
    Hauk O, Stenroos M.  
    A framework for the design of flexible cross-talk functions for spatial  
    filtering of EEG/MEG data: DeFleCT.  
    Human Brain Mapping 2013  
    http://imaging.mrc-cbu.cam.ac.uk/meg/AnalyzingData/DeFleCT_SpatialFiltering_Tools  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_inverse_minimumnorm.m)
  """

  return Runtime.call("bf_inverse_minimumnorm", *args, **kwargs)
