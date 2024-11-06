from spm.__wrapper__ import Runtime


def spm_voronoi(*args, **kwargs):
    """
      Geodesic Discrete Voronoi Diagram - a compiled routine  
        FORMAT [vor, dist] = spm_voronoi(img, seeds, distance)  
         
        img       - binary image:  > 0  : inside  
                                   <= 0 : outside   
        seeds     - {n x 3} array of the n seeds positions [in voxels]  
        distance  - type of chamfer distance to use ('d4', 'd8', 'd34' or 'd5711')  
                    (default is 'd34')  
         
        vor       - Geodesic Discrete Voronoi diagram   
                    (label is equal to the index of the seed in 'seeds')  
        dist      - Geodesic Distance map of img with seeds as objects  
         
        Compute the geodesic discrete Voronoi Diagram of an image of labelled   
        objects using front propagation. The distance map is also available   
        on output.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_voronoi.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_voronoi", *args, **kwargs)
