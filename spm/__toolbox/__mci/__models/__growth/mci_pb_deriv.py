from spm.__wrapper__ import Runtime


def mci_pb_deriv(*args, **kwargs):
    """
      Gradient of log-likelihood for Preece-Baines model  
        FORMAT [dLdp,iCpY,L] = mci_pb_deriv (P,M,U,Y)  
         
        dLdp      gradient of log joint  
        iCpY      curvature (Fisher Information)  
        L         log joint  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/models/growth/mci_pb_deriv.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mci_pb_deriv", *args, **kwargs)
