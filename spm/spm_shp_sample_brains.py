from spm.__wrapper__ import Runtime


def spm_shp_sample_brains(*args, **kwargs):
    """
      FORMAT  [z,z0,mesh] = spm_shp_sample_brains(mesh, K, ...)  
         
        Positional  
        ----------  
        mesh   - (N x 1) Mesh(es) to deform (gifti objects or paths).  
        K      - Number of brains to make [default: 1]  
         
        Keywords  
        --------  
        pc     - Vector of indices principal components to use [default: all]  
        span   - Latent bound(s) [default: [0 ,3] ]  
        fout   - Folder where to write generated gifti files [default: '.']  
        fshp   - Folder where the shape model is stored.  
        suffix - Output file suffix [default: 0]  
        v0     - Subject's initial velocity [default: 0]  
        y0     - Subject's transform [default: recompute]  
        z0     - Subject's latent code [default: recompute]  
        r2n    - Subject's import to native transform [default: identity]  
        can    - If true:  center samples about canonical brain (z=0)  
                 If false: center samples about subject's brain (z=z0)  
         
        Returns  
        -------  
        z       - (M x K) Sampled latent codes  
        z0      - (M x 1) Subject's latent code  
        outmesh - (K x N) Deformed mesh(es) (gifti or paths)  
         
        Some PC indices can be negative meaning their pca components (2) will be  
        linearly shifted in opposite direction, i.e. [1 2] and [1 -2] are two  
        different trajectories where 2nd component moves in opposite direction.  
       ______________________________  ____________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_shp_sample_brains.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_shp_sample_brains", *args, **kwargs)
