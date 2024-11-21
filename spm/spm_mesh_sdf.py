from spm.__wrapper__ import Runtime


def spm_mesh_sdf(*args, **kwargs):
    """
      Compute the signed distance field (SDF) to a triangle mesh  
        FORMAT D = spm_mesh_sdf(M, V, m)  
        M        - a patch structure with fields 'faces' and 'vertices'  
        V        - an spm_vol structure with fields 'dim' and 'mat'  
        m        - a binary mask (image filename or spm_vol structure)  
                   [default: none]  
         
        F        - a 3D array containing signed distance values  
       __________________________________________________________________________  
         
        Example:  
         
        M = gifti(fullfile(spm('Dir'),'canonical','cortex_20484.surf.gii'));  
        M = export(M,'patch');  
        M.faces = double(M.faces);  
        V = spm_vol(fullfile(spm('Dir'),'canonical','single_subj_T1.nii'));  
         
        F = spm_mesh_sdf(M, V);  
         
        D = struct(...  
            'fname',   'sdf.nii',...  
            'dim',     V.dim,...  
            'dt',      [spm_type('float64') spm_platform('bigend')],...  
            'mat',     V.mat,...  
            'pinfo',   [1 0 0]');  
        spm_write_vol(D, F);  
         
        spm_check_registration(D.fname);  
        spm_ov_mesh('Display', 1, M);  
        spm_colourmap('hot')  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_mesh_sdf.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mesh_sdf", *args, **kwargs)
