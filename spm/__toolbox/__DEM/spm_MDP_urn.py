from spm.__wrapper__ import Runtime


def spm_MDP_urn(*args, **kwargs):
    """
      Demo for active inference with the urn task  
       __________________________________________________________________________  
         
        This demonstration uses the Urn or Beads Task to illustrate how choice  
        behaviour can be simulated using active inference - in the context of  
        Markov decision processes. In the urn task, a succession of draws  
        from one of two urns are made and the agent has to decide whether the  
        balls are being drawn from an urn with predominantly red or green balls.  
        We model this in terms of a state-space with four dimensions: number of  
        balls drawn (n),  number of green balls drawn (k), choice (undecided, red   
        or green)and the true (hidden) state of the urn (red or green). With  
        this relatively simple state-space, the utility of any hidden state is  
        simply quantified by the log-odds ratio of making a correct  
        decision. From binomial theory this is (2k - n)*log(p/(1 - p)), where p  
        is the proportion of red or green balls. Having defined the utility  
        function of states, we can then use the MDP formulation of active  
        inference using variational Bayes to simulate choice behaviour.   
         
        This routine first provides an illustration of a game in which a decision  
        is delayed until the last draw to look at inferences during successive  
        draws - with a special focus on precision. The illustration here shows  
        a decrease in precision when an unexpected (green ball) is drawn during a  
        sequence of red balls.  
         
        We then characterise changes in choice probability (and latency to the  
        decision) in terms of its dependency on threshold criteria (on the odds  
        ratio) and hyperpriors about precision (alpha or the scale parameter of a   
        standard gamma distribution). The routine concludes with an illustration   
        of how to estimate model parameters using the likelihood of observed  
        (simulated) choices.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_MDP_urn.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_MDP_urn", *args, **kwargs, nargout=0)
