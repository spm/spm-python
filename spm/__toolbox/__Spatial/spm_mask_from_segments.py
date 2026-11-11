from spm._runtime import Runtime


def spm_mask_from_segments(*args, **kwargs):
    r"""
     ==========================================================================  
        brain extraction/masking script using spm segment tool  
        it sums three probability maps from segment tool, thresholds the resulting map to obtain binary mask and fills residual holes  
        Inputs:  
        mag_file      - file from which to estimate the mask  
        thresh        - between 0 and 1, smaller value bigger mask, threshold of the spm probability maps to create a binary map  
        fill_holes    - true or false, if true it will fill small holes within the mask  
        conn          - used in imfill.m, connectivity of neighbouring voxels, choose one of the following: 4, 6, 8, 18, 26  
        mask_mag      - true or false, if true it will also output masked mag_file  
         
        Outputs:  
        mask_file     - file path from the output mask  
        mask          - 3D binary mask matrix  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/Spatial/spm_mask_from_segments.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mask_from_segments", *args, **kwargs)
