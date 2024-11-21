from spm.__wrapper__ import Runtime


def DEM_MDP_decision(*args, **kwargs):
    """
      Demo of active inference for visual salience  
       __________________________________________________________________________  
         
        This routine illustrates the treatment of signal detection paradigms in  
        the context of active inference and Markov decision processes. This is  
        probably one of the simplest paradigms to model; in which there are just  
        too  hidden states generating ambiguous stimuli - and the agent move from  
        an undecided (hidden) state to a definitive choice. The A tensor in this  
        instanceen codes ambiguity (perceptual noise), while the B matrix encodes  
        the behaviour-dependent transitions among decision states. Finally,  
        the C matrix  encodes  prior costs or preferences. In this instance, the  
        agent does not want to be wrong - and prefers to be right.  
         
        in what follows, we simulate a single trial to illustrate the underlying  
        Bayesian belief updating and associated behavioural and physiological  
        responses. We then consider multiple trials under different levels of  
        ambiguity and cost. The dependent measures in this instance include the  
        behavioural accuracy, reaction times (assuming 250 ms time bins) and the  
        uncertainty about the cause of sensory cues and control - as measured by  
        the entropy of posterior beliefs prior to making a choice.  
         
        see also: DEM_demo_MDP_rule.m and spm_MPD_VB_X.m  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_MDP_decision.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_MDP_decision", *args, **kwargs)
