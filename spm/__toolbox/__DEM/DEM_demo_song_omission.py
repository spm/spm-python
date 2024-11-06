from spm.__wrapper__ import Runtime


def DEM_demo_song_omission(*args, **kwargs):
    """
      Demo for bird songs: In this example, we show that DEM can not only  
        estimate the hidden states of an autonomous system but can also  
        deconvolve dynamic changes in its control parameters.  We illustrate  
        this using a slow Lorentz attractor to drive a fast one; both showing  
        deterministic chaos.  We endow the simulations with a little ethological  
        validity by using the states of the fast Lorentz attractor as control  
        variables in the syrinx of a song bird (usually these would control a van  
        der Pol oscillator model). We will look at the true and inferred songs  
        with and without the last chirps missing.  The sonograms displayed  
        can be played by a mouse click on the image.  Subsequent plots show  
        simulated event-related potential to show that there is a marked  
        responses (prediction error) of the system when an expected 'syllable' is  
        omitted. This demonstrates the implicit sequence-decoding of input  
        streams, using generative models based upon attractors.  
        Having simulated normal omission-related responses, we then reduce the  
        precision at the second level (on both hidden causes and states) and  
        repeat the simulation. The result is an attenuation of the omission-  
        related response or mismatch negativity. If we try to compensate by  
        reducing the sensory precision, then the autonomous dynamics predicting  
        the sequence of chirps supervenes, producing false inference. This  
        can be thought of as a - crude - model of hallucinosis.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_demo_song_omission.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_demo_song_omission", *args, **kwargs, nargout=0)
