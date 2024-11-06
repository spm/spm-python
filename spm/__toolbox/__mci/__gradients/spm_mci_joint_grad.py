from spm.__wrapper__ import Runtime


def spm_mci_joint_grad(*args, **kwargs):
    """
      Gradient of Log Joint Probability  
        FORMAT [j,iCpY,st,L,L2] = spm_mci_joint_grad (Pr,M,U,Y)  
         
        Pr        parameters (vectorised and in M.V subspace)  
        M         model structure. If field .beta is specified this  
                  sets the inverse temperature to beta (default=1)  
        U         inputs  
        Y         data  
         
        j         gradient of log joint, dL/dP   
        iCpY      Curvature (Fisher Information)  
        st        Status flag (0 for OK, -1 for problem)  
        L         log joint, L = log p(Y,P)  
        L2        log likelihood, L2 = log p(Y|P)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/gradients/spm_mci_joint_grad.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mci_joint_grad", *args, **kwargs)
