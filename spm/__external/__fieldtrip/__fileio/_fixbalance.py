from spm._runtime import Runtime


def _fixbalance(*args, **kwargs):
    r"""
      FIXBALANCE ensures that the balancing representation in grad.balance or  
        elec.balance field is up to date and consistent, specifically with the  
        list of linear projections (or montages) being applied specified as  
        cell-array in "current", and not as a string in "current" and cell-array  
        in "previous".  
         
        See also FT_DATATYPE_SENS  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/fixbalance.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fixbalance", *args, **kwargs)
