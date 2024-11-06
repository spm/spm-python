from spm.__wrapper__ import Runtime


def DEM_demo_duet(*args, **kwargs):
    """
      This demonstration uses active inference (as implemented in spm_ALAP) to  
        illustrate birdsong and communication using predictive coding. In this  
        example, priors on high-level sensorimotor constructs (e.g., in the  
        avian higher vocal centre) are used to generate proprioceptive  
        predictions (i.e., motor commands) so that the bird can sing. However, in  
        the absence of sensory attenuation, the slight differences between  
        descending predictions and the sensory consequences of self-made songs  
        confound  singing. This means that sensory attenuation is required so  
        that the bird can either sing or listen.  By introducing a second bird  
        and alternating between singing and listening respectively, one can  
        simulate communication through birdsong. This is illustrated with one  
        cycle of singing and listening, where the high level expectations about  
        hidden states become synchronised; in effect, the two birds are singing  
        from the same 'hymn sheet' or narrative and can be regarded as  
        communicating in the sense of pragmatics. The first bird's expectations  
        are shown in red, while the second bird's are shown in cyan.  
         
        To simulate learning of each other's (high-level) attractor, set LEARN to  
        one in the  main script.. To separate the birds - and preclude  
        communication (or synchronisation chaos) set NULL to 1.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_demo_duet.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_demo_duet", *args, **kwargs, nargout=0)
