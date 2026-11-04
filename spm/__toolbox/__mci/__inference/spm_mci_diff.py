from spm._runtime import Runtime


def spm_mci_diff(*args, **kwargs):
    r"""
      Compute gradient and curvature of log likelihood using finite differences  
        FORMAT [dLdp,iCpY,L] = spm_mci_diff (P,M,U,Y)  
         
        dLdp      gradient of log likelihood  
        iCpY      curvature (observed Fisher Information)  
        L         log likelihood  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mci/inference/spm_mci_diff.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mci_diff", *args, **kwargs)
