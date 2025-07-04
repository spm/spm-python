from spm._runtime import Runtime


def DEM_demo_MDP_search(*args, **kwargs):
    """
      Demo of active inference for visual salience  
       __________________________________________________________________________  
         
        This routine uses active inference for Markov decision processes to  
        illustrate epistemic foraging in the context of visual searches. Here,  
        the agent has to categorise scenes on the basis of the relative position  
        of various cues. Crucially, the agent can only sample one cue or location  
        at a time and therefore has to accumulate evidence for competing  
        hypotheses. This rests upon resolving uncertainty about which scene or  
        hypothesis is in play through the minimisation of expected free energy.  
         
        When the agent become sufficiently confident about the underlying scene,  
        it then makes a saccade to a choice location - to obtain feedback (right  
        or wrong). The agent prefers to be right and does not expect to be  
        wrong. We first illustrate a single trial in terms of behaviour and  
        electrophysiological responses. We then consider sequences of trials and  
        how average behaviour (accuracy, number of saccades and saccade duration)  
        depends upon prior preferences and prior precision.  
         
        This demonstration uses a factorised version of the MDP scheme. In  
        other words, we assume a mean field approximation to the posterior over  
        different hidden states (context, location, scene reflection) - and over  
        multiple modalities (what versus where).  This provides a parsimonious  
        representation of posterior beliefs over hidden states - but does induce  
        degree of overconfidence associated with approximate Bayesian inference.  
         
        see also: DEM_demo_MDP_habits.m and spm_MPD_VB_X.m  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_demo_MDP_search.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("DEM_demo_MDP_search", *args, **kwargs)
