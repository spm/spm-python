from spm.__wrapper__ import Runtime


def spm_MDP_offer(*args, **kwargs):
    """
      Demo for active inference with limited offer game  
       __________________________________________________________________________  
         
        This demonstration routine uses variational Bayes to minimise the free  
        energy to model decision-making. The particular focus here is on  
        decisions that are time-sensitive, requiring an explicit representation  
        of future states. The example considered here represents a limited offer  
        game, where a low offer can be converted to a high offer, which may or  
        may not occur. Furthermore, offers may be withdrawn. The objective is  
        to understand model choices about accepting or declining the current  
        offer in terms of active inference, under prior beliefs about future  
        states. The model is specified in a fairly general way in terms of  
        probability transition matrices and beliefs about future states. The  
        particular inversion scheme used here is spm_MDP_game, which uses a  
        mean-field approximation between hidden control and hidden states. It is  
        assumed that the agent believes that it will select a particular action  
        (accept or decline) at a particular time.  
         
        We run an exemplar game, examine the distribution of time to acceptance  
        as a function of different beliefs (encoded by parameters of the  
        underlying Markov process) and demonstrate how the model can be used to  
        produce trial-specific changes in uncertainty - or how one can use  
        behaviour to identify the parameters used by a subject.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_MDP_offer.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_MDP_offer", *args, **kwargs, nargout=0)
