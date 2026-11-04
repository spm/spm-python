from spm._runtime import Runtime


def mci_compare_setup(*args, **kwargs):
    r"""
      Set up data structures for fwd/sens/grad comparisons  
        FORMAT [P,M,U,Y,ind] = mci_compare_setup (model)  
         
        model     'phase', 'nmm-r2p2'  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mci/gradients/mci_compare_setup.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mci_compare_setup", *args, **kwargs)
