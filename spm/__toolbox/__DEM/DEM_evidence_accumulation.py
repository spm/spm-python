from spm.__wrapper__ import Runtime


def DEM_evidence_accumulation(*args, **kwargs):
    """
      Saccadic eye movements under active inference:  
       __________________________________________________________________________  
        This demo illustrates evidence accumulation (and responses) using a very  
        simple generative model. In this model, there are three hidden states  
        corresponding to right motion, no motion and left motion - as registered  
        uniformly over 16 visual channels. Motion is slowly introduced, which  
        moves the hidden states to one of the unstable fixed points; thereby  
        inducing proprioceptive predictions that cause a motor response. The  
        generative model is as minimal as possible and is based on generalised  
        Lotka-Volterra dynamics to emulate a dynamic form of winner takes all. In  
        other words, the only prior beliefs of this generative model are that the  
        world can be in one of a number of (unstable) states. Evidence is  
        accumulated slowly because the input is noisy (and is assigned a low  
        precision). This reveals the evidence accumulation dynamics that drive  
        action, when inference is sufficiently confident. These dynamics are  
        formally equivalent to the race or drift diffusion dynamics in normative  
        (descriptive) formulations of evidence accumulation.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_evidence_accumulation.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_evidence_accumulation", *args, **kwargs)
