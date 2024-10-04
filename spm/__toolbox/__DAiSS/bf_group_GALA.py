from spm.__wrap__ import _Runtime


def bf_group_GALA(*args, **kwargs):
  """  Computes Minimum Norm projectors  
     
    Please cite:  
    Hauk O, Stenroos M.  
    A framework for the design of flexible cross-talk functions for spatial  
    filtering of EEG/MEG data: DeFleCT.  
    Human Brain Mapping 2013  
    http://imaging.mrc-cbu.cam.ac.uk/meg/AnalyzingData/DeFleCT_SpatialFiltering_Tools  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_group_GALA.m)
  """

  return _Runtime.call("bf_group_GALA", *args, **kwargs)
