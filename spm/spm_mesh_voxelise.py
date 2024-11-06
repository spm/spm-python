from spm.__wrapper__ import Runtime


def spm_mesh_voxelise(*args, **kwargs):
    """
      Voxelise a triangle mesh on a regular grid  
        FORMAT [R, V] = spm_mesh_voxelise(M, V)  
        M        - a patch structure or GIfTI object  
        V        - structure with fields 'dim' and 'mat' defining the grid  
                   or voxel size for automatic field of view [default: 1]  
         
        R        - logical array: 1 for inside and 0 for outside  
       __________________________________________________________________________  
         
        M = gifti(fullfile(spm('Dir'),'canonical','cortex_5124.surf.gii'));  
        V = spm_vol(fullfile(spm('Dir'),'canonical','avg152T1.nii'));  
        R = spm_mesh_voxelise(M, V);  
        V.fname = 'voxelised.nii';  
        V.dt(1) = spm_type('uint8');  
        V.pinfo = [1 0 0]';  
        V.dat = uint8(R);  
        spm_check_registration(V)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_mesh_voxelise.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mesh_voxelise", *args, **kwargs)
