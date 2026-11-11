from spm._runtime import Runtime


def spm_mesh_to_grid(*args, **kwargs):
    r"""
      Non-linear interpolation of surface-based data onto a regular grid  
        FORMAT R = spm_mesh_to_grid(M, V, T)  
        M        - a patch structure with fields 'faces' and 'vertices'  
        V        - an spm_vol structure with fields 'dim' and 'mat'  
        T        - array of data to be interpolated  
         
        R        - interpolated data on grid defined by V  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_mesh_to_grid.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mesh_to_grid", *args, **kwargs)
