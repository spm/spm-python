from spm.__wrapper__ import Runtime


def ft_trialfun_trial(*args, **kwargs):
  """  FT_TRIALFUN_TRIAL creates a trial definition that corresponds to the events that  
    are returned by FT_READ_EVENT with type='trial'  
     
    Use this function by calling  
      [cfg] = ft_definetrial(cfg)  
    where the configuration structure should contain  
      cfg.dataset           = string with the filename  
      cfg.trialfun          = 'ft_trialfun_trial'  
     
    See also FT_DEFINETRIAL, FT_TRIALFUN_GENERAL  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/trialfun/ft_trialfun_trial.m)
  """

  return Runtime.call("ft_trialfun_trial", *args, **kwargs)
