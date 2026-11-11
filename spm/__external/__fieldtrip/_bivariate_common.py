from spm._runtime import Runtime


def _bivariate_common(*args, **kwargs):
    r"""
      BIVARIATE_COMMON makes a selection for a specific reference channel from a  
        bivariate (i.e. connectivity) dataset and returns that selection as a univariate  
        dataset. This is used in singleplot/multiplot/topoplot for both ER and TFR data.  
         
        Use as  
          [varargout] = bivariate_common(cfg, varargin)  
         
        See also TOPOPLOT_COMMON  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/bivariate_common.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("bivariate_common", *args, **kwargs)
