from spm.__wrapper__ import Runtime


def DEMO_MDP_questions(*args, **kwargs):
    """
      Demo of active inference for visual salience  
       __________________________________________________________________________  
         
        This routine provide simulations of reading to demonstrate deep temporal  
        generative models. It builds upon the scene construction simulations to  
        equip the generative model with a second hierarchical level. In effect,  
        this creates an agent that can accumulate evidence at the second level  
        based upon epistemic foraging at the first. In brief, the agent has to  
        categorise a sentence or narrative into one of two categories (happy or  
        sad), where it entertains six possible sentences. Each sentence comprises  
        four words, which are themselves constituted by two pictures or graphemes  
        These are the same visual outcomes used in previous illustrations of  
        scene construction and saccadic searches.  
         
        Here, the agent has policies at two levels. The second level policy (with  
        just one step into the future) allows it to either look at the next word  
        or stay on the current page and make a decision. Concurrently, a first  
        level policy entails one of four saccadic eye movements to each quadrant  
        of the current page, where it will sample a particular grapheme.  
         
        This provides a rough simulation of reading - that can be made more  
        realistic by terminating first level active inference, when there can be  
        no further increase in expected free energy (i.e., all uncertainty about  
        the current word has been resolved). The subsequent inferred hidden  
        states then become the outcome for the level above.  
         
        To illustrate the schemes biological plausibility, one can change the  
        agent's prior beliefs and repeat the reading sequence under violations of  
        either local (whether the graphemes are flipped vertically) or globally  
        (whether the sentence is surprising) expectations. This produces a  
        mismatch negativity (MMN) under local violations) and a MMN with a  
        P300 with global violations.  
         
        see also: DEM_demo_MDP_habits.m and spm_MPD_VB_X.m  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEMO_MDP_questions.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEMO_MDP_questions", *args, **kwargs)
