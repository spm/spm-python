from spm.__wrapper__ import Runtime


def _triangulate_seg(*args, **kwargs):
    """
      TRIANGULATE_SEG constructs a triangulation of the outer surface of a segmented  
        volume. It starts at the center of the volume and projects the vertices of an  
        evenly triangulated sphere onto the outer surface. The resulting surface is by  
        construction star-shaped from the origin of the sphere.  
         
        Use as  
          [pnt, tri] = triangulate_seg(seg, npnt, origin)  
         
        Input arguments:  
         seg    = 3D-matrix (boolean) containing the segmented volume  
         npnt   = requested number of vertices  
         origin = 1x3 vector specifying the location of the origin of the sphere  
                  in voxel indices. This argument is optional. If undefined, the  
                  origin of the sphere will be in the centre of the volume.  
         
        Output arguments:  
         pnt = Nx3 matrix of vertex locations  
         tri = Mx3 matrix of triangles  
         
        The segmentation will be checked for holes, and filled if necessary. Also, the  
        segmentation will be checked to consist of a single boolean blob. If not, only the  
        outer surface of the largest will be triangulated. SPM is used for both the filling  
        and checking for multiple blobs.  
         
        See also MESH_SPHERE  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/triangulate_seg.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("triangulate_seg", *args, **kwargs)
