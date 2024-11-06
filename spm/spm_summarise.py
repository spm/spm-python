from spm.__wrapper__ import Runtime


def spm_summarise(*args, **kwargs):
    """
      Summarise data within a Region of Interest  
        FORMAT [Y, xY] = spm_summarise(V,xY,fhandle)  
        V       - [1 x n] vector of mapped image volumes to read (from spm_vol)  
                  Or a char array of filenames  
        xY      - VOI structure (from spm_ROI)  
                  Or a VOI_*.mat (from spm_regions) or a mask image filename  
                  Or the keyword 'all' to summarise all voxels in the images  
                  Or a [3 x m] matrix of voxel coordinates {mm}  
        fhandle - function handle to be applied on image data within VOI  
                  Must transform a [1 x m] array into a [1 x p] array  
                  Default is Identity (returns raw data, vectorised into rows).  
                  Can also use keyword 'litres' to compute the total volume,  
                  within the region of interest, for a tissue segment image.  
         
        Y       - [n x p] data summary  
        xY      - (updated) VOI structure  
       __________________________________________________________________________  
         
        Example:  
        spm_summarise('beta_0001.nii',...  
                      struct('def','sphere', 'spec',8, 'xyz',[10 20 30]'),...  
                      @mean)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_summarise.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_summarise", *args, **kwargs)
