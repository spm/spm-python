from spm._runtime import Runtime


def setCTFDataBalance(*args, **kwargs):
    r"""
       Version 1.1  13 April 2007  Mod to chanList:  If chanList is omitted and  
                                     size(data,2)<ds.res4.no_channels, then setCTFDataBalance  
                                     sets chanList=1:size(data,2) and prints a warning the first  
                                     time it happens.  
                      7 Dec. 2006.   Fixed a bug.  Changed calls to getCTFBalanceCoefs so   
                      setCTFDataBalance would balance and unbalance reference gradiometers.  
         Version 1.0   27 October 2006  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/ctf/setCTFDataBalance.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("setCTFDataBalance", *args, **kwargs)
