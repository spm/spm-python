from spm.__wrapper__ import Runtime


def pm_seed(*args, **kwargs):
    """
      Find a suitable (hopefully) seed point from which  
        to start watershed-based unwrapping.  
        FORMAT: seed = pm_seed(angvar,mask,pxs)  
         
        Input:  
        angvar  : Map of variance of (voxelwise) estimates  
                  of phase angle.  
        mask    : Tells us which part of angvar to consider.  
        pxs     : Array of voxel sizes, used to ensure  
                  isotropic smoothing.  
         
        Output:  
        seed    : Coordinates of suitable seed point.  
         
        In order to find a seed point we first threshold the  
        variance map at a quarter of the variance of a U(-pi,pi)  
        distribution. This gives us a binary image with ones only  
        for low variance regions. This is then smoothed with a  
        very wide gaussian kernel (50mm). The maximum of  
        the smoothed map is then pretty much a centre-of-mass  
        of the "low-variance volume". It could however in  
        principle be a relatively high variance voxel  
        surrounded by low-variance voxels. Therefore we pick  
        a percentage of the highest voxels in the smooth map  
        (i.e. we pick a neighbourhood) and then pick the location  
        of those that has the lowest variance in the original  
        variance map.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/FieldMap/pm_seed.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("pm_seed", *args, **kwargs)
