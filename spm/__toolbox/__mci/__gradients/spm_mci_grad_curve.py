from spm.__wrapper__ import Runtime


def spm_mci_grad_curve(*args, **kwargs):
    """
      Compute gradient and curvature for MFX model  
        FORMAT [dLdp,iCpY,st] = spm_mci_grad_curve (assign,w,v,M,U,Y,fxtype)  
         
        assign    fields specify which are random/fixed effects  
        w         random effects vector  
        v         fixed effects vector  
        M,U,Y     structure,inputs,data  
        fxtype    'random' or 'fixed'  
         
        dLdp      gradient  
        iCpY      curvature (Fisher information)  
        st        -1 for integration problem  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/gradients/spm_mci_grad_curve.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mci_grad_curve", *args, **kwargs)
