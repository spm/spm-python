from spm.__wrapper__ import Runtime


def spm_affreg(*args, **kwargs):
    """
      Affine registration using least squares  
        FORMAT [M,scal] = spm_affreg(VG,VF,flags,M0,scal0)  
         
        VG        - Vector of template volumes.  
        VF        - Source volume.  
        flags     - a structure containing various options.  The fields are:  
                    WG       - Weighting volume for template image(s).  
                    WF       - Weighting volume for source image  
                               Default to [].  
                    sep      - Approximate spacing between sampled points (mm).  
                               Defaults to 5.  
                    regtype  - regularisation type.  Options are:  
                               'none'  - no regularisation  
                               'rigid' - almost rigid body  
                               'subj'  - inter-subject registration (default).  
                               'mni'   - registration to ICBM templates  
                    globnorm - Global normalisation flag (1)  
        M0        - (optional) starting estimate. Defaults to eye(4).  
        scal0     - (optional) starting estimate.  
         
        M         - affine transform, such that voxels in VF map to those in  
                    VG by   VG.mat\M*VF.mat  
        scal      - scaling factors for VG  
         
        When only one template is used, then the cost function is approximately  
        symmetric, although a linear combination of templates can be used.  
        Regularisation is based on assuming a multi-normal distribution for the  
        elements of the Henckey Tensor. See:  
        "Non-linear Elastic Deformations". R. W. Ogden (Dover), 1984.  
        Weighting for the regularisation is determined approximately according  
        to:  
        "Incorporating Prior Knowledge into Image Registration"  
        J. Ashburner, P. Neelin, D. L. Collins, A. C. Evans & K. J. Friston.  
        NeuroImage 6:344-352 (1997).  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/OldNorm/spm_affreg.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_affreg", *args, **kwargs)
