from spm._runtime import Runtime


def mci_discount_deriv(*args, **kwargs):
    r"""
      Gradient of likelihood for discounting model  
        FORMAT [dLdp,iCpY,L] = mci_discount_deriv (P,M,U,Y)  
         
        P         parameters  
        M         model structure  
        U         contains rewards and times  
        Y         data  
         
        dLdp      gradient of log joint  
        iCpY      curvature (Fisher Information)  
        L         log joint  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mci/models/discount/mci_discount_deriv.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mci_discount_deriv", *args, **kwargs)
