from spm._runtime import Runtime


def mci_compare_forward(*args, **kwargs):
    r"""
      Compare integration methods   
        FORMAT [els_sun,els_ode,els_spm] = mci_compare_forward (model)  
         
        model     'phase', 'nmm-r2p2'  
         
        Run integration 9 times - compare speed and accuracy  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mci/demo-gradients/mci_compare_forward.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mci_compare_forward", *args, **kwargs)
