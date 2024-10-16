from spm.__wrapper__ import Runtime


def _bivariate_common(*args, **kwargs):
  """  BIVARIATE_COMMON makes a selection for a specific reference channel from a  
    bivariate (i.e. connectivity) dataset and returns that selection as a univariate  
    dataset. This is used in singleplot/multiplot/topoplot for both ER and TFR data.  
     
    Use as  
      [varargout] = bivariate_common(cfg, varargin)  
     
    See also TOPOPLOT_COMMON  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/bivariate_common.m)
  """

  return Runtime.call("bivariate_common", *args, **kwargs)
