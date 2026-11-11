from spm._runtime import Runtime


def ft_read_vol(*args, **kwargs):
    r"""
      This function is a backward compatibility wrapper for existing MATLAB scripts  
        that call a function that is not part of the FieldTrip toolbox any more.  
         
        Please update your code to make it future-proof.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/ft_read_vol.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_read_vol", *args, **kwargs)
