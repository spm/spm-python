from spm.__wrapper__ import Runtime


def _warp_hermes2010(*args, **kwargs):
    """
      WARP_HERMES2010 projects the ECoG grid / strip onto a cortex hull  
        using the algorithm described in Hermes et al. (2010,  
        J Neurosci methods) in which electrodes are projected onto the pial  
        surface using the orthogonal local norm vector to the grid. To align ECoG   
        electrodes to the pial surface, you first need to compute the cortex hull   
        with FT_PREPARE_MESH.  
         
        See also FT_ELECTRODEREALIGN, FT_PREPARE_MESH, WARP_DYKSTRA2012  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/warp_hermes2010.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("warp_hermes2010", *args, **kwargs)
