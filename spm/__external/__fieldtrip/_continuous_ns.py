from spm.__wrap__ import _Runtime


def _continuous_ns(*args, **kwargs):
  """  CONTINUOUS_NS created a trial definition from a Neuroscan *.cnt file  
    which subsequently can be used in the EEG/MEG framework  
     
    Use as  
      [trl] = continuous_ns(cfg)  
     
    where the configuration should contain   
      cfg.trialdef.trigger  = number or list with triggers  
      cfg.trialdef.prestim  = pre-stimulus in seconds  
      cfg.trialdef.poststim = post-stimulus in seconds      
     
    See also SINGLETRIAL_NS  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/continuous_ns.m)
  """

  return _Runtime.call("continuous_ns", *args, **kwargs)
