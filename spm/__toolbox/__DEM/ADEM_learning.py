from spm.__wrapper__ import Runtime


def ADEM_learning(*args, **kwargs):
    """
      Value learning demo using the mountain car problem. This demo questions  
        the need for reinforcement learning and related paradigms from  
        machine-learning, when trying to optimise the behaviour of an agent.  We  
        show that it is fairly simple to teach an agent complicated and adaptive  
        behaviours under the free-energy principle.  This principle suggests that  
        agents adjust their internal states and sampling of the environment to  
        minimize their free-energy.  In this context, free-energy represents a  
        bound on the probability of being in a particular state, given the nature  
        of the agent, or more specifically the model of the environment an agent  
        entails.  We show that such agents learn causal structure in the  
        environment and sample it in an adaptive and self-supervised fashion.  
        The result is a behavioural policy that reproduces exactly the policies  
        that are optimised by reinforcement learning and dynamic programming.  
        Critically, at no point do we need to invoke the notion of reward, value  
        or utility.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/ADEM_learning.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ADEM_learning", *args, **kwargs, nargout=0)
