from spm.__wrapper__ import Runtime


def spm_mesh_normals(*args, **kwargs):
    """
      Compute (unit) normals of a surface mesh  
        FORMAT [Nv, Nf] = spm_mesh_normals(M, unit)  
        M      - a patch structure or a handle to a patch  
        unit   - boolean to indicate unit normals or not [default: false]  
         
        Nv     - a [nx3] array of (unit) normals on vertices  
        Nf     - a [mx3] array of (unit) normals on faces  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_mesh_normals.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mesh_normals", *args, **kwargs)
