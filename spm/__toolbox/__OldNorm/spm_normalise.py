from spm.__wrapper__ import Runtime


def spm_normalise(*args, **kwargs):
    """
      Spatial (stereotactic) normalization  
         
        FORMAT params = spm_normalise(VG,VF,matname,VWG,VWF,flags)  
        VG        - template handle(s)  
        VF        - handle of image to estimate params from  
        matname   - name of file to store deformation definitions  
        VWG       - template weighting image  
        VWF       - source weighting image  
        flags     - flags.  If any field is not passed, then defaults are assumed.  
                    smosrc - smoothing of source image (FWHM of Gaussian in mm).  
                             Defaults to 8.  
                    smoref - smoothing of template image (defaults to 0).  
                    regtype - regularisation type for affine registration  
                              See spm_affreg.m (default = 'mni').  
                    cutoff  - Cutoff of the DCT bases.  Lower values mean more  
                              basis functions are used (default = 30mm).  
                    nits    - number of nonlinear iterations (default=16).  
                    reg     - amount of regularisation (default=0.1)  
        _________________________________________________________________________  
          
        This module spatially (stereotactically) normalizes MRI, PET or SPECT  
        images into a standard space defined by some ideal model or template  
        image[s].  The template images supplied with SPM conform to the space  
        defined by the ICBM, NIH P-20 project, and approximate that of the  
        the space described in the atlas of Talairach and Tournoux (1988).  
        The transformation can also be applied to any other image that has  
        been coregistered with these scans.  
         
          
        Mechanism  
        Generally, the algorithms work by minimising the sum of squares  
        difference between the image which is to be normalised, and a linear  
        combination of one or more template images.  For the least squares  
        registration to produce an unbiased estimate of the spatial  
        transformation, the image contrast in the templates (or linear  
        combination of templates) should be similar to that of the image from  
        which the spatial normalization is derived.  The registration simply  
        searches for an optimum solution.  If the starting estimates are not  
        good, then the optimum it finds may not find the global optimum.  
          
        The first step of the normalization is to determine the optimum  
        12-parameter affine transformation.  Initially, the registration is  
        performed by matching the whole of the head (including the scalp) to  
        the template.  Following this, the registration proceeded by only  
        matching the brains together, by appropriate weighting of the template  
        voxels.  This is a completely automated procedure (that does not  
        require ``scalp editing'') that discounts the confounding effects of  
        skull and scalp differences.   A Bayesian framework is used, such that  
        the registration searches for the solution that maximizes the a  
        posteriori probability of it being correct.  i.e., it maximizes the  
        product of the likelihood function (derived from the residual squared  
        difference) and the prior function (which is based on the probability  
        of obtaining a particular set of zooms and shears).  
          
        The affine registration is followed by estimating nonlinear deformations,  
        whereby the deformations are defined by a linear combination of three  
        dimensional discrete cosine transform (DCT) basis functions.  
        The parameters represent coefficients of the deformations in  
        three orthogonal directions.  The matching involved simultaneously  
        minimizing the bending energies of the deformation fields and the  
        residual squared difference between the images and template(s).  
          
        An option is provided for allowing weighting images (consisting of pixel  
        values between the range of zero to one) to be used for registering  
        abnormal or lesioned brains.  These images should match the dimensions  
        of the image from which the parameters are estimated, and should contain  
        zeros corresponding to regions of abnormal tissue.  
          
          
        Uses  
        Primarily for stereotactic normalization to facilitate inter-subject  
        averaging and precise characterization of functional anatomy.  It is  
        not necessary to spatially normalise the data (this is only a  
        pre-requisite  for  intersubject averaging or reporting in the  
        Talairach space).  
          
        Inputs  
        The first input is the image which is to be normalised. This image  
        should be of the same modality (and MRI sequence etc) as the template  
        which is specified. The same spatial transformation can then be  
        applied to any other images of the same subject.  These files should  
        conform to the SPM data format (See 'Data Format'). Many subjects can  
        be entered at once, and there is no restriction on image dimensions  
        or voxel size.  
          
        Providing that the images have a correct ".mat" file associated with  
        them, which describes the spatial relationship between them, it is  
        possible to spatially normalise the images without having first  
        resliced them all into the same space. The ".mat" files are generated  
        by "spm_realign" or "spm_coregister".  
          
        Default values of parameters pertaining to the extent and sampling of  
        the standard space can be changed, including the model or template  
        image[s].  
          
          
        Outputs  
        All normalized *.img scans are written to the same subdirectory as  
        the original *.img, prefixed with a 'n' (i.e. n*.img).  The details  
        of the transformations are displayed in the results window, and the  
        parameters are saved in the "*_sn.mat" file.  
          
       __________________________________________________________________________  
         
        References:  
        K.J. Friston, J. Ashburner, C.D. Frith, J.-B. Poline, J.D. Heather,  
        and R.S.J. Frackowiak  
        Spatial Registration and Normalization of Images.  
        Human Brain Mapping 2:165-189, 1995.  
          
        J. Ashburner, P. Neelin, D.L. Collins, A.C. Evans and K.J. Friston  
        Incorporating Prior Knowledge into Image Registration.  
        NeuroImage 6:344-352, 1997.  
         
        J. Ashburner and K.J. Friston  
        Nonlinear spatial normalization using basis functions.  
        Human Brain Mapping, 7(4):254-266, 1999.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/OldNorm/spm_normalise.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_normalise", *args, **kwargs)
