from spm.__wrapper__ import Runtime


def _prepare_mesh_cortexhull(*args, **kwargs):
    """
      PREPARE_MESH_CORTEXHULL creates a mesh representing the cortex hull, i.e.  
        the smoothed envelope around the pial surface created by FreeSurfer  
         
        This function relies on the FreeSurfer and iso2mesh software packages  
         
        Configuration options:  
          cfg.headshape    = a filename containing the pial surface computed by  
                             FreeSurfer recon-all ('/path/to/surf/lh.pial')  
          cfg.fshome       = FreeSurfer folder location  
                             (default: '/Applications/freesurfer')  
          cfg.resolution   = resolution of the volume delimited by headshape being  
                             floodfilled by mris_fill (default: 1)  
          cfg.outer_surface_sphere = diameter of the sphere used by make_outer_surface  
                             to close the sulci using morphological operations (default: 15)  
          cfg.smooth_steps = number of standard smoothing iterations (default: 0)  
          cfg.laplace_steps = number of Laplacian (non-shrinking) smoothing  
                             iterations (default: 2000)  
          cfg.fixshrinkage = reduce possible shrinkage due to smoothing (default: 'no')  
          cfg.expansion_mm = amount in mm with which the hull is re-expanded, applies  
                             when cfg.fixshrinkage = 'yes' (default: 'auto')  
         
        See also FT_PREPARE_MESH  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/prepare_mesh_cortexhull.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("prepare_mesh_cortexhull", *args, **kwargs)
