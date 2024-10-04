from spm.__wrap__ import _Runtime


def mne_rt_define_commands(*args, **kwargs):
  """   
       [ FIFF ] = mne_rt_define_commands()  
     
       Defines structure containing the MNE_RT constants  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/mne_rt_define_commands.m)
  """

  return _Runtime.call("mne_rt_define_commands", *args, **kwargs)
