from spm.__wrapper__ import Runtime


def spm_MDP_trust(*args, **kwargs):
    """
      Demo of active inference for trust games  
       __________________________________________________________________________  
         
        This routine uses the Markov decision process formulation of active  
        inference (with variational Bayes) to model a simple trust game. In trust  
        games, one plays an opponent who can either cooperate or defect. The  
        payoff contingencies depend upon the joint choices of you and your  
        opponent, which in turn depend upon your inferences about the nature of  
        the opponent (pro-social or non-social). This example illustrates single  
        round games with a special focus on Bayesian belief updating between  
        games. This is illustrated in terms of evidence accumulation about  
        the nature of the opponent by using the posterior marginal distributions  
        following one game as the prior distribution over beliefs about the  
        opponent in the next. This accumulation is shown in the final figures.  
         
        In this example, there are nine states. The first is a starting state  
        and the subsequent eight states model the four combinations of  
        cooperation and defection (between you and your opponent) under the  
        prior beliefs that the opponent is either pro-social or non-social.   
        Initially, these prior beliefs are uninformative but are subsequently   
        informed through experience. prior beliefs about behaviour are based on  
        relative entropy or KL divergence in the usual way - which requires the  
        specification of utility functions over states based upon standard payoff  
        tables in these sorts of games. It is interesting to see how precision  
        or confidence in beliefs about choices, fluctuates with beliefs about  
        the nature of one's opponent.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_MDP_trust.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_MDP_trust", *args, **kwargs, nargout=0)
