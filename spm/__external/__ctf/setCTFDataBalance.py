from spm.__wrapper__ import Runtime


def setCTFDataBalance(*args, **kwargs):
    """
       Version 1.1  13 April 2007  Mod to chanList:  If chanList is omitted and  
                                     size(data,2)<ds.res4.no_channels, then setCTFDataBalance  
                                     sets chanList=1:size(data,2) and prints a warning the first  
                                     time it happens.  
                      7 Dec. 2006.   Fixed a bug.  Changed calls to getCTFBalanceCoefs so   
                      setCTFDataBalance would balance and unbalance reference gradiometers.  
         Version 1.0   27 October 2006  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/ctf/setCTFDataBalance.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("setCTFDataBalance", *args, **kwargs)
