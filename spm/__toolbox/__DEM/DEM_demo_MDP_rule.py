from spm.__wrapper__ import Runtime


def DEM_demo_MDP_rule(*args, **kwargs):
    """
      Demo of active inference for visual salience  
       __________________________________________________________________________  
         
        This routine simulates a crude form of consciousness using active  
        inference and structure learning to vitiate ignorance or nescience. This  
        entails learning the hyperparameters of causal structure generating  
        outcomes and then using Bayesian model reduction (during sleep) to  
        minimise complexity.  
         
        We first set up an abstract problem in which an agent has to respond  
        according to rules (identify the correct colour depending upon one of  
        three rules that are specified by the colour of a cue in the centre of  
        vision). If the rule is centre, the colour is always green; however, if  
        the colour of the Centre cue is red, the correct colour is on the left  
        (and on the right if the queue is blue). Simulations are provided when  
        the agent knows the rules. This is then repeated in the absence  
        (nescience) of any knowledge about the rules to see if the agent can  
        learn causal structure through Bayesian belief updating of the likelihood  
        array (A).  
         
        We then consider the improvement in performance (in terms of variational  
        free energy, its constituent parts and performance) following Bayesian  
        model reduction of the likelihood model (heuristically, like slow wave  
        sleep), followed by a restitution of posterior beliefs during fictive  
        active inference (as in REM sleep). Finally, we address the communication  
        of the implicit  structure learning to a conspecific or child to  
        demonstrate the improvement under instruction.  
         
        see also: DEM_demo_MDP_habits.m and spm_MPD_VB_X.m  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_demo_MDP_rule.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_demo_MDP_rule", *args, **kwargs)
