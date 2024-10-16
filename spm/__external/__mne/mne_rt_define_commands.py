from spm.__wrapper__ import Runtime


def mne_rt_define_commands(*args, **kwargs):
  """   
       [ FIFF ] = mne_rt_define_commands()  
     
       Defines structure containing the MNE_RT constants  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/mne_rt_define_commands.m)
  """

  return Runtime.call("mne_rt_define_commands", *args, **kwargs)
