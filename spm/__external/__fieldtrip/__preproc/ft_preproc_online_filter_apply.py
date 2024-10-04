from spm.__wrap__ import _Runtime


def ft_preproc_online_filter_apply(*args, **kwargs):
  """  FT_PREPROC_ONLINE_FILTER_APPLY passes a signal through the online filter and  
    returns the updated filter model (delay states) and the filtered signal.  
     
    Use as  
      [state, dat] = ft_preproc_online_filter_apply(state, dat)  
    where  
      dat   = Nchan x Ntime  
      state = filter state, see FT_PREPROC_ONLINE_FILTER_INIT  
     
    See also PREPROC  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/preproc/ft_preproc_online_filter_apply.m)
  """

  return _Runtime.call("ft_preproc_online_filter_apply", *args, **kwargs)
