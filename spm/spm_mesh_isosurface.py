from spm.__wrapper__ import Runtime


def spm_mesh_isosurface(*args, **kwargs):
    """
      Compute isosurface geometry from volume data  
        FORMAT M = spm_mesh_isosurface(V, t, s)  
        V        - volume data  
                   spm_vol struct, nifti object or 3D array  
        t        - isosurface value  
        s        - Gaussian filter width (FWHM) in {edges} [Default: 0]  
         
        M        - patch structure  
         
        This is merely a wrapper around isosurface.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_mesh_isosurface.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mesh_isosurface", *args, **kwargs)
