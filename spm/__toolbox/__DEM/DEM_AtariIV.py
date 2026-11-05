from spm._runtime import Runtime


def DEM_AtariIV(*args, **kwargs):
    r"""
      de novo Structure learning — of pullback attractors —  afrom pixels   
       __________________________________________________________________________  
         
        This routine illustrates the de novo learning of a state action policy —  
        and goal-directed behaviour using inductive inference under the ensuing  
        model. The approach is based upon the fast structure learning of dynamics  
        (i.e., transitions among generalised or deep states) that possess a  
        nonequilibrium steady-state distribution (NESS). This is guaranteed when  
        all states are transient states on a (pullback) attractor. In this  
        example, random play is generated for 10,000 frames of a simplified  
        arcade game. These are used to learn the structure of a renormalising  
        generative model; namely, the recursive composition of states and paths  
        specified by edges or dependencies (i.e., indices of parents). The  
        resulting structure is then used to accumulate sequences of random play  
        that, by chance, include rewarded outcomes. Following this active  
        selection the training data are used to accumulate  
        transitions to, and only to, the basins of attraction of goal states.  
        When all goal states lie in a basin of attraction — of other goal states  
        — the accumulation terminates. At this point, the dynamics possess a  
        nonequilibrium steady-state, which is used to reduce the model by  
        pruning away redundant states.  
         
        This demonstration features an efficient self-[Eigen]reduction, using  
        the nonequilibrium steady-state distribution to evaluate the expected  
        reward. Generalised states are removed if the (analytic) gradient of  
        expected cost — with respect to the probability of transitions to the  
        state in question — is positive.  
         
        The ensuing model is then demonstrated in generative mode by generating  
        (perfect) fantasy play. The model is then used for real gameplay by  
        installing the generative process in the model and using explicit action  
        to learn from any mistakes: inductive inference is used to find the path  
        of least action from one goal state to the next and new paths are  
        retained, provided they do not incur any costs. Finally, the model is  
        demonstrated after a final reduction or compression by retaining deep  
        (generalised) states that predict current and future actions.  
         
        This form of de novo structure learning uses a generative model that  
        generates predictions in multiple streams. The principal (leading) stream  
        generates pixel data, while subsequent streams generate rewards, costs  
        and the consequences of action (e.g., proprioception or telemetry). By  
        having separate streams, one can find an efficient or reduced model that  
        preserves the mutual information between generalised states at the  
        highest level and future action. These deep states are effectively  
        multimodal and serve to couple pixel level states to action; thereby  
        affording an efficient state action policy — that is realised through  
        inductive inference.  
       __________________________________________________________________________  
        Copyright (C) 2019 Wellcome Trust Centre for Neuroimaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/DEM_AtariIV.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("DEM_AtariIV", *args, **kwargs)
