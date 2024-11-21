from spm.__wrapper__ import Runtime


def mci_compare_jacobians(*args, **kwargs):
    """
      Compare user supplied and finite difference methods  
        FORMAT [Fx,Fp,FxFD,FpFD] = mci_compare_jacobians (model)  
         
        model     'phase'  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/demo-gradients/mci_compare_jacobians.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mci_compare_jacobians", *args, **kwargs)
