from spm._runtime import Runtime


def mci_compare_jacobians(*args, **kwargs):
    r"""
      Compare user supplied and finite difference methods  
        FORMAT [Fx,Fp,FxFD,FpFD] = mci_compare_jacobians (model)  
         
        model     'phase'  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mci/demo-gradients/mci_compare_jacobians.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mci_compare_jacobians", *args, **kwargs)
