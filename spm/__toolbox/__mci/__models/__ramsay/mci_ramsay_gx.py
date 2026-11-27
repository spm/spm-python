from spm._runtime import Runtime


def mci_ramsay_gx(*args, **kwargs):
    r"""
      Observation equation for Ramsay model  
        FORMAT [y,L] = spm_ramsay_gx (x,u,P,M)  
         
        x,u,P,M     state,input,params,model  
         
        y           observations  
        L           dy/dx  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mci/models/ramsay/mci_ramsay_gx.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_ramsay_gx", *args, **kwargs)
