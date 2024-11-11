from spm.__wrapper__ import Runtime


def mci_compare_setup(*args, **kwargs):
    """
      Set up data structures for fwd/sens/grad comparisons  
        FORMAT [P,M,U,Y,ind] = mci_compare_setup (model)  
         
        model     'phase', 'nmm-r2p2'  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/gradients/mci_compare_setup.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mci_compare_setup", *args, **kwargs)
