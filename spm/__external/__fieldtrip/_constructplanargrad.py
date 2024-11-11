from spm.__wrapper__ import Runtime


def _constructplanargrad(*args, **kwargs):
    """
      CONSTRUCTPLANARGRAD constructs a planar gradiometer array from an axial gradiometer  
        definition. This can be used to compute the planar field gradient for a known  
        (estimated) source configuration.  
          
        Use as  
          [grad_planar] = constructplanargrad(cfg, grad_axial)  
         
        Where cfg contains the following configuration details  
          cfg.baseline_axial   = number (default is 5)  
          cfg.baseline_planar  = number (default is 0.5)  
          cfg.planaraxial      = 'no' or 'yes' (default)  
          
        The option planaraxial='yes' specifies that the planar gradiometers  
        should consist of axial gradiometers, to make them comparable with  
        Ole Jensens planar gradient computation. If planaraxial='no', the  
        planar gradiometers will be more or less similar to the Neuromag  
        system.  
         
        The input grad can be a CTF type axial gradiometer definition, but  
        just as well be a magnetometer definition. This function only assumes  
        that  
          grad.coilpos  
          grad.coilori  
          grad.label  
        exist and that the first Nlabel channels in pnt and ori should be  
        used to compute the position of the coils in the planar gradiometer  
        channels.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/constructplanargrad.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("constructplanargrad", *args, **kwargs)
