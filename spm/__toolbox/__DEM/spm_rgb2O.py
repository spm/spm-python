from spm._runtime import Runtime


def spm_rgb2O(*args, **kwargs):
    r"""
      RGB image format to discrete outcomes (O)  
        FORMAT [O,L,RGB] = spm_rgb2O(I);  
          
        I    - RGB image (pixels x pixels x 3 colours x time): uint8  
         
        RGB.nd  - Diameter of tiles in pixels [default: 32]  
        RGB.nb  - Number of discrete singular variates  [9: must be odd]    
        RGB.mm  - Maximum number of singular modes      [32]  
        RGB.su  - Singular value (normalised) threshold [16]  
        RGB.R   - temporal resampling                   [2]  
         
        O    - Cell array of probabilistic outputs for pixel partition  
        L    - Location of each probabilistic output modality  
         
        RBG  - structure containing image size, pixel locations, singular vectors  
               and bins for singular variates  
         
        RGB.M   - locations of groups  
        RGB.N   - image size  
        RGB.G   - cell array of outcome indices  
        RGB.V   - singular vectors  
        RGB.A   - singular variates  
        RGB.O   - group index  
         
        This routine effectively learns a basis set or receptive fields for a  
        sequence of images supplied in RGB like format. It uses singular value  
        decomposition, retaining the principal singular vectors for subsequent  
        compression and reconstruction. The singular variates discretised over  
        the range of each variate. The ensuing amortisation is saved in RGB  
        structure for image reconstruction. This version uses overlapping  
        receptive fields during the grouping and applies a Gaussian window around  
        the centroid of each group location.  
         
        Crucially, these spatial grouping operators can be generalised to  
        spatiotemporal grouping by specifying a temporal resampling rate. In  
        other words, one can discretise short image sequences.  
         
        If the basis set has already been evaluated, this routine will return the  
        discretised space-time voxels of any image timeseries, based upon the  
        pre-evaluated spatial grouping and singular vectors.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_rgb2O.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_rgb2O", *args, **kwargs)
