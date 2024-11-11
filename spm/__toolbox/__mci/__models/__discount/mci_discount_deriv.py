from spm.__wrapper__ import Runtime


def mci_discount_deriv(*args, **kwargs):
    """
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/models/discount/mci_discount_deriv.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mci_discount_deriv", *args, **kwargs)
