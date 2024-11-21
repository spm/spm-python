from spm.__wrapper__ import Runtime


def spm_mesh_project(*args, **kwargs):
    """
      Project volumetric data onto a mesh  
        FORMAT P = spm_mesh_project(M, dat, method)  
        M        - a patch structure, a handle to a patch   
                   or a [nx3] vertices array  
        dat      - a structure array [1xm] with fields dim, mat, XYZ and t   
                   (see spm_render.m)  
                   or a structure array [1xm] with fields mat and dat  
                   or a structure array [1xm] from spm_vol.m  
                   or a char array/cellstr of image filenames  
        method   - interpolation method {'nn'}  
        varargin - other parameters required by the interpolation method  
         
        P        - a [mxn] projected data array  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_mesh_project.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mesh_project", *args, **kwargs)
