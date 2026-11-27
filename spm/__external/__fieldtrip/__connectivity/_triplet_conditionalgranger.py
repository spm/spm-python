from spm._runtime import Runtime


def _triplet_conditionalgranger(*args, **kwargs):
    r"""
      TRIPLET_CONDITIONALGRANGER  
          
        Inputs:  
          H3,Z3: transfer matrix, noise covariance for  
            triplets, 3x3(xtriplet)xnfreq  
          H2,Z2: transfer matrix, noise covariance for  
            duplets,  2x2(xnduplet)xnfreq  
          cmbindx: Nx3 indices determining the output, abc = b->a/c  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/connectivity/private/triplet_conditionalgranger.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("triplet_conditionalgranger", *args, **kwargs)
