from spm.__wrapper__ import Runtime


def _warp_dykstra2012(*args, **kwargs):
    """
      WARP_DYKSTRA2012 projects the ECoG grid / strip onto a cortex hull  
        using the algorithm described in Dykstra et al. (2012, Neuroimage) in   
        which the distance from original positions and the deformation of the   
        grid are minimized. This function relies on MATLAB's optimization toolbox.   
        To align ECoG electrodes to the pial surface, you first need to compute   
        the cortex hull with FT_PREPARE_MESH.  
         
        Additional configuration options to the original functionality  
          cfg.maxiter       = number (default: 50), maximum number of optimization   
                              iterations  
          cfg.pairmethod    = 'pos' (default) or 'label', the method for electrode  
                              pairing on which the deformation energy is based  
          cfg.isodistance   = 'yes', 'no' (default) or number, to enforce isotropic  
                              inter-electrode distances (pairmethod 'label' only)  
          cfg.deformweight  = number (default: 1), weight of deformation relative   
                              to shift energy cost (lower increases grid flexibility)  
         
        See also FT_ELECTRODEREALIGN, FT_PREPARE_MESH, WARP_HERMES2010  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/warp_dykstra2012.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("warp_dykstra2012", *args, **kwargs)
