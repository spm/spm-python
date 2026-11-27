from spm._runtime import Runtime


def DEM_Pong(*args, **kwargs):
    r"""
      Demo of planning as sophisticated inference (Tower of Hanoi)  
       __________________________________________________________________________  
         
        This routine demonstrates the acquisition of self organised behaviour  
        using a simulated game of ping-pong. It starts by illustrating the  
        emergence of game play during the acquisition of a likelihood model under  
        precise beliefs about transitions through latent states. These  
        transitions are generic and describe a (long) orbit with circular  
        boundary conditions. This allows the agent to map successive states to  
        observable outcomes. In this simulation the outcomes can be regarded as  
        pixels (that can be on or off). In the particular set up here, a ball  
        bounces around inside a box, while a paddle can be moved at the bottom  
        right or left. Whenever there is a failure to hit the ball, unpredictable  
        stimuli are delivered to all outcomes. This reflects an ambiguity that is  
        specific to latent states under which the ball does not fall on the  
        paddle. This ambiguity is, effectively, aversive; leading the agent to  
        return the ball for short rallies, after it has acquired the requisite  
        likelihood mapping (i.e., learned about the ambiguous outcomes).  
          
        We then repeat the simulation but making the box wider and therefore  
        making the ball more difficult to track. This slows down learning and  
        subsequent skilled gameplay. In the final simulation, this is rescued  
        using inductive inference. With inductive constraints on active  
        inference, skilled performance becomes fluent after about 512 timesteps  
        (i.e., about two minutes of simulated time).  
          
        The depth of planning in the simulations is set to N = 1; i.e., looking  
        ahead to time steps. The agents have mild preferences for not being  
        overly stimulated; i.e., C{g} = spm_softmax([0;1]).  
       __________________________________________________________________________  
        Copyright (C) 2019 Wellcome Trust Centre for Neuroimaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/DEM_Pong.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("DEM_Pong", *args, **kwargs)
