from spm.__wrap__ import _Runtime


def mne_ex_rt(*args, **kwargs):
  """   
      An example of a mne_rt_server real-time connection  
     
      function mne_ex_rt(mne_rt_server_ip, mne_rt_server_commandPort ,mne_rt_server_fiffDataPort)  
     
      mne_rt_server_ip           - IP of the running mne_rt_server  
      mne_rt_server_commandPort  - Command port of the mne_rt_server  
      mne_rt_server_fiffDataPort - Fiff data port of the mne_rt_server  
     
      Returns the measurement info  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/mne_ex_rt.m)
  """

  return _Runtime.call("mne_ex_rt", *args, **kwargs)
