from spm._runtime import Runtime


def spm_MDP_breakout(*args, **kwargs):
    r"""
      Creates an MDP structure for a simple game of Breakout  
        FORMAT [MDP,hid,cid,con,RGB] = spm_MDP_breakout(Nr,Nc,Nd)  
       --------------------------------------------------------------------------  
        Nr                     % number of rows  
        Nc                     % number of columns  
        Nd                     % randomness of resets  
        hid   - Hidden states corresponding to hits  
        cid   - Hidden states corresponding to misses  
        con   - output modalities reporting control  
        RGB   - display structure  
         
        outcomes(1) - paddle  
        outcomes(2) - ball  
        outcomes(3) - target centre  
        outcomes(4) - target periphery  
        outcomes(5) - background  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_MDP_breakout.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_MDP_breakout", *args, **kwargs)
