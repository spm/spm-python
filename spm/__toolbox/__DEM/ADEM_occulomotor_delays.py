from spm.__wrapper__ import Runtime


def ADEM_occulomotor_delays(*args, **kwargs):
    """
      Oculomotor following and delays under active inference:  
       __________________________________________________________________________  
        This demo illustrates oculomotor following and slow pursuit. The focus  
        here is on oculomotor delays and their compensation in generalised  
        coordinates of motion. This is illustrates using a 'sweep' of motion to  
        examine the effects of motor delays, sensory delays and their interaction  
        under active inference. We then move on to oculomotor following of sine  
        wave motion, in which the trajectory entrains following under compensated  
        dynamics. This entrainment can be destroyed by rectifying the sine wave  
        which calls for a more realistic (hierarchical) model of motion that  
        registers its phase and anticipates the next onset of motion (cf  
        movement behind an occluder). These simulations depend delicately on  
        delays and precisions (gains) that are chosen to make oculomotor following  
        under uncertainty relatively slow. The dependency on visual uncertainty  
        (contrast) is illustrated by changing the precision of the generalised  
        motion of the sensory target.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/ADEM_occulomotor_delays.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ADEM_occulomotor_delays", *args, **kwargs, nargout=0)
