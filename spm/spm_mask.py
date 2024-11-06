from spm.__wrapper__ import Runtime


def spm_mask(*args, **kwargs):
    """
      Mask images  
        FORMAT spm_mask(P1, P2, thresh)  
        P1     - matrix of input image filenames from which  
                 to compute the mask.  
        P2     - matrix of input image filenames on which  
                 to apply the mask.  
        thresh - optional threshold(s) for defining the mask.  
        The masked images are prepended with the prefix `m'.  
         
        If any voxel in the series of images is zero (for data types without  
        a floating point representation) or does not have a finite value (for  
        floating point and double precision images), then that voxel is set to  
        NaN or zero in all the images.  If a threshold, or vector of  
        thresholds is passed, then the masking is based on voxels whos  
        values are above all the thresholds.  
         
        Images sampled in different orientations and positions can be passed  
        to the routine.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_mask.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mask", *args, **kwargs, nargout=0)
