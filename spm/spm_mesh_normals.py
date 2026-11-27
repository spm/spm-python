from spm._runtime import Runtime


def spm_mesh_normals(*args, **kwargs):
    r"""
      Compute (unit) normals of a surface mesh  
        FORMAT [Nv, Nf] = spm_mesh_normals(M, unit)  
        M      - a patch structure or a handle to a patch  
        unit   - boolean to indicate unit normals or not [default: false]  
         
        Nv     - a [nx3] array of (unit) normals on vertices  
        Nf     - a [mx3] array of (unit) normals on faces  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_mesh_normals.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mesh_normals", *args, **kwargs)
