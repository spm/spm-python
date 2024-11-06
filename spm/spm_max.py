from spm.__wrapper__ import Runtime


def spm_max(*args, **kwargs):
    """
      Sizes, maxima and locations of local excursion sets  
        FORMAT [N Z M A XYZ] = spm_max(X,L)  
        X     - values of 3-D field  
        L     - locations [x y z]' {in voxels}  
         
        N     - size of region {in voxels)  
        Z     - Z values of maxima  
        M     - location of maxima {in voxels}  
        A     - region number  
        XYZ   - cell array of voxel locations  
       __________________________________________________________________________  
         
        spm_max characterizes a point list of voxel values (X) and their  
        locations (L) in terms of edge, face and vertex connected subsets,  
        returning a maxima- orientated list:  The value of the ith maximum is  
        Z(i) and its location is given by M(:,i). A(i) identifies the ith  
        maximum with a region. Region A(i) contains N(i) voxels, whose  
        coordinates are in a 3-by-N(i) array in XYZ{i}.  
         
        See also: spm_bwlabel.m and spm_clusters.m  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_max.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_max", *args, **kwargs)
