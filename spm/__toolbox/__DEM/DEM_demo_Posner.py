from spm.__wrapper__ import Runtime


def DEM_demo_Posner(*args, **kwargs):
    """
      This demonstration routine simulates the Posner paradigm to show that   
        some of the characteristic speed-accuracy trade-offs associated with   
        valid and invalid cueing can be explained easily in terms of optimizing   
        precisions during hierarchical inference. This demonstration uses   
        generalised filtering and state-space model that includes state-dependent  
        noise. Here, this dependency is used to set the attentional gain or bias   
        using a cue, which modulates the prediction errors induced by subsequent   
        targets. The phenomena that emerge from this scheme include a competition  
        for attentional resources; given that only one context can exist at any   
        time and this probabilistic context is encoded by state-dependent   
        precisions on the causes of sensory input. Attended stimuli have greater   
        precision and greater penetration of their prediction errors in the   
        hierarchy. We will also see characteristic differences between perceptual   
        inference, under valid and invalid cues. This is illustrated using   
        simulated psychophysical and electrophysiological responses. Biased   
        competition is simulated by presenting both valid and invalid targets   
        simultaneously.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_demo_Posner.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_demo_Posner", *args, **kwargs, nargout=0)
