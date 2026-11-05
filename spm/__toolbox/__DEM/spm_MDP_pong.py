from spm._runtime import Runtime


def spm_MDP_pong(*args, **kwargs):
    r"""
      Creates an MDP structure for a simple game of Pong  
        FORMAT [MDP,hid,cid,con,RGB,nP] = spm_MDP_pong(Nr,Nc,Nd,Na,Np)  
       --------------------------------------------------------------------------  
        Nr    - number of rows  
        Nc    - number of columns  
        Nd    - number of initial states [default: 1]  
        Na    - returns rewards, costs and action  
        Np    - number of distractor pixels  
         
        hid   - Hidden states corresponding to hits  
        cid   - Hidden states corresponding to misses  
        con   - output modalities reporting control  
        RGB   - display structure  
         
        outcomes(1) - ball  
        outcomes(2) - bat (right)  
        outcomes(3) - bat (centre)  
        outcomes(4) - bat (left)  
        outcomes(5) - background  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_MDP_pong.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_MDP_pong", *args, **kwargs)
