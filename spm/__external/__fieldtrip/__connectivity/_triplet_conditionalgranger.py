from spm.__wrapper__ import Runtime


def _triplet_conditionalgranger(*args, **kwargs):
    """
      TRIPLET_CONDITIONALGRANGER  
          
        Inputs:  
          H3,Z3: transfer matrix, noise covariance for  
            triplets, 3x3(xtriplet)xnfreq  
          H2,Z2: transfer matrix, noise covariance for  
            duplets,  2x2(xnduplet)xnfreq  
          cmbindx: Nx3 indices determining the output, abc = b->a/c  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/connectivity/private/triplet_conditionalgranger.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("triplet_conditionalgranger", *args, **kwargs)
