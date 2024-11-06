from spm.__wrapper__ import Runtime


def ADEM_plaid(*args, **kwargs):
    """
      creates a Gaussian modulated n x n visual plaid stimulus  
        FORMAT [y,n] = ADEM_plaid(x,[n])  
        x(1) - horizontal displacement  
        x(2) - vertical displacement  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/ADEM_plaid.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ADEM_plaid", *args, **kwargs)
