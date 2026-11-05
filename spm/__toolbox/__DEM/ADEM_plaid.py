from spm._runtime import Runtime


def ADEM_plaid(*args, **kwargs):
    r"""
      creates a Gaussian modulated n x n visual plaid stimulus  
        FORMAT [y,n] = ADEM_plaid(x,[n])  
        x(1) - horizontal displacement  
        x(2) - vertical displacement  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/ADEM_plaid.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ADEM_plaid", *args, **kwargs)
