from spm.__wrapper__ import Runtime


def spm_MDP(*args, **kwargs):
    """
      solves the active inference problem for Markov decision processes  
        FROMAT [Q,R,S,U,P] = spm_MDP(MDP)  
         
        MDP.T           - process depth (the horizon)  
        MDP.S(N,1)      - initial state  
        MDP.B{M}(N,N)   - transition probabilities among hidden states (priors)  
        MDP.C(N,1)      - terminal cost probabilities (prior N over hidden states)  
        MDP.D(M,1)      - control probabilities (prior over M control states)  
         
        optional:  
         
        MDP.W           - log-precision of beliefs about transitions (default: 1)  
        MDP.G{M}(N,N)   - transition probabilities used to generate outcomes  
                          (default: the prior transition probabilities)  
        MDP.A(N,N)      - Likelihood of outcomes given hidden states  
                          (default: an identity mapping from states to outcomes)  
        MDP.B{T,M}(N,N) - transition probabilities for each time point  
        MDP.G{T,M}(N,N) - transition probabilities for each time point  
                          (default: MDP.B{T,M} = MDP.B{M})  
         
        MDP.plot        -  swtich to suppress graphics  
         
        produces:  
         
        Q(N,K,T) - an array of conditional (posterior) expectations over N hidden  
                   states and time 1,...,T at time 1,...,K  
        R(M,K,T) - an array of conditional expectations over M control  
                   states and time 1,...,T at time 1,...,K  
        S(N,T)   - a sparse matrix of ones, encoding the state at time 1,...,T  
        U(M,T)   - a sparse matrix of ones, encoding the action at time 1,...,T  
        P(M,T)   - probabaility of emitting action 1,...,M at time 1,...,T  
         
        This routine provides solutions of active inference (minimisation of  
        variational free energy)using a generative model based upon a Markov  
        decision process. This model and inference scheme is formulated  
        in discrete space and time. This means that the generative model (and  
        process) are  finite state  machines or hidden Markov models whose  
        dynamics are given by transition probabilities among states. For  
        simplicity, we assume an isomorphism between hidden states and outcomes,  
        where the likelihood corresponds to a particular outcome conditioned upon  
        hidden states. Similarly, for simplicity, this routine assumes that action  
        and hidden controls are isomorphic. If the dynamics of transition  
        probabilities of the true process are not provided, this routine will use  
        the equivalent probabilities from the generative model.  
         
        The transition probabilities are a cell array of probability transition  
        matrices corresponding to each (discrete) the level of the control state.  
         
        Mote that the conditional expectations are functions of time but also  
        contain expectations about fictive states over time at each time point.  
        To create time dependent transition probabilities, one can specify a  
        function in place of the transition probabilities under different levels  
        of control.  
         
        partially observed Markov decision processes can be modelled by  
        specifying a likelihood (as part of a generative model) and absorbing any  
        probabilistic mapping between (isomorphic) hidden states and outcomes  
        into the transition probabilities G.  
         
        See also spm_MDP_game  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_MDP.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_MDP", *args, **kwargs)
