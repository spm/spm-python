from spm.__wrapper__ import Runtime


def spm_mesh_dist(*args, **kwargs):
    """
      Compute signed or unsigned distance from a point to a triangle mesh  
        FORMAT D = spm_mesh_dist(M, XYZ, S)  
        M        - a patch structure with fields 'faces' and 'vertices'  
        XYZ      - a n x 3 array of points coordinates {mm}  
        S        - logical scalar for signed or unsigned distances  
                   [default: true, i.e. signed]  
         
        D        - a n x 1 vector of signed or unsigned distances from XYZ to M  
       __________________________________________________________________________  
         
        Based on C++ library:  
        https://github.com/InteractiveComputerGraphics/TriangleMeshDistance  
        Copyright (c) 2021 Jose Antonio Fernandez Fernandez, MIT license  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_mesh_dist.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mesh_dist", *args, **kwargs)
