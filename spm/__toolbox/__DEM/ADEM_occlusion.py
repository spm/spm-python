from spm.__wrapper__ import Runtime


def ADEM_occlusion(*args, **kwargs):
    """
      Slow pursuit and occlusion under active inference:  
       __________________________________________________________________________  
        This demo illustrates slow pursuit in the context of visual occlusion. We  
        start with a simulation of canonical slow pursuit of a visual target   
        with sine wave motion. Crucially, the generative model is equipped with   
        a simple empirical prior encoding the hidden motion of the target (using   
        a linear oscillator, whose frequency is determined by a hidden cause).   
        We then examine failures of tracking and anticipation during occlusion   
        and when the target re-emerges from behind the occluder. We look at a   
        simulation in which the precision of the oscillator dynamics modelling   
        long-term behaviour of the target is reduced (cf., neuromodulatory   
        deficits in cortical areas encoding biological motion). This has a   
        an effect of producing a failure of pursuit, resulting in a catch-up  
        saccade on target reappearance. The suppression of prior precision can  
        however have beneficial effects when motion is itself unpredicted  
        (as shown with differential pursuit performance under a reversal of   
        the trajectory towards the end of motion). Finally, we look at how prior   
        beliefs are acquired during exposure to the target - in terms of   
        cumulative inference on the hidden causes encoding the frequency of   
        periodic motion. This can be regarded as a high order form of evidence   
        accumulation. Importantly, this (experience-dependent) inference is  
        markedly impaired by the simulated lesion to precision above. In other   
        words, a single failure of inference in modelling the motion of hidden   
        states can have secondary consequences - such as a failure to even   
        register and remember regularities. All these simulations are based upon   
        active inference; with the prior belief that the centre of gaze is   
        attracted to the same point responsible for target motion.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/ADEM_occlusion.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ADEM_occlusion", *args, **kwargs, nargout=0)
