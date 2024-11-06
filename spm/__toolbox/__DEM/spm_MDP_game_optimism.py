from spm.__wrapper__ import Runtime


def spm_MDP_game_optimism(*args, **kwargs):
    """
      aaction selection using active inference (with optimism bias)  
        FORMAT [MDP] = spm_MDP_game_optimism(MDP,OPTION)  
         
        MDP.T           - process depth (the horizon)  
        MDP.N           - number of variational iterations (default 4)  
        MDP.S(N,1)      - true initial state  
         
        MDP.A(O,N)      - Likelihood of O outcomes given N hidden states  
        MDP.B{M}(N,N)   - transition probabilities among hidden states (priors)  
        MDP.C(N,1)      - terminal cost probabilities (prior over outcomes)  
        MDP.D(N,1)      - initial prior probabilities (prior over hidden states)  
         
        MDP.V(T,P)      - P allowable policies (control sequences over T times)  
         
        optional:  
        MDP.s(1 x T)    - vector of true states  - for deterministic solutions  
        MDP.o(1 x T)    - vector of observations - for deterministic solutions  
        MDP.a(1 x T)    - vector of action       - for deterministic solutions  
        MDP.w(1 x T)    - vector of precisions   - for deterministic solutions  
         
        MDP.B{T,M}(N,N) - model transition probabilities for each time point  
        MDP.G{T,M}(N,N) - true  transition probabilities for each time point  
                          (default: MDP.G{T,M} = MDP.G{M} = MDP.B{M})  
         
        MDP.plot        - switch to suppress graphics: (default: [0])  
        MDP.alpha       - upper bound on precision (Gamma hyperprior - shape [8])  
        MDP.beta        - precision over precision (Gamma hyperprior - rate  [1])  
         
        produces:  
         
        MDP.P(M,T)   - probability of emitting an action 1,...,M at time 1,...,T  
        MDP.Q(N,T)   - an array of conditional (posterior) expectations over  
                       N hidden states and time 1,...,T  
        MDP.O(O,T)   - a sparse matrix of ones encoding outcomes at time 1,...,T  
        MDP.S(N,T)   - a sparse matrix of ones encoding states at time 1,...,T  
        MDP.U(M,T)   - a sparse matrix of ones encoding action at time 1,...,T  
        MDP.W(1,T)   - posterior expectations of precision  
        MDP.d        - simulated dopamine responses  
         
        OPTION       - {'Free Energy' | 'KL Control' | 'Expected Utility'};  
         
        This routine provides solutions of active inference (minimisation of  
        variational free energy) using a generative model based upon a Markov  
        decision process. This model and inference scheme is formulated  
        in discrete space and time. This means that the generative model (and  
        process) are  finite state machines or hidden Markov models whose  
        dynamics are given by transition probabilities among states and the  
        likelihood corresponds to a particular outcome conditioned upon  
        hidden states. For simplicity, this routine assumes that action  
        and hidden controls are isomorphic. If the dynamics of transition  
        probabilities of the true process are not provided, this routine will use  
        the equivalent probabilities from the generative model.  
         
        This implementation equips agents with the prior beliefs that they will  
        maximise expected free energy: expected free energy is the free energy  
        of future outcomes under the posterior predictive distribution. This can  
        be interpreted in several ways - most intuitively as minimising the KL  
        divergence between predicted and preferred outcomes (specified as prior  
        beliefs) - while simultaneously minimising the (predicted) entropy of   
        outcomes conditioned upon hidden states. Expected free energy therefore  
        combines KL optimality based upon preferences or utility functions with  
        epistemic value or information gain.  
         
        This particular scheme is designed for any allowable policies or control  
        sequences specified in MDP.V. Constraints on allowable policies can limit  
        the numerics or combinatorics considerable. For example, situations in  
        which one action can be selected at one time can be reduced to T polices  
        - with one (shift) control being emitted at all possible time points.  
        This specification of polices simplifies the generative model, allowing a  
        fairly exhaustive model of potential outcomes - eschewing a mean field  
        approximation over successive control states. In brief, the agent simply  
        represents the current state and states in the immediate and distant  
        future.  
         
        The transition probabilities are a cell array of probability transition  
        matrices corresponding to each (discrete) the level of the control state.  
         
        Mote that the conditional expectations are functions of time but also  
        contain expectations about fictive states over time at each time point.  
        To create time dependent transition probabilities, one can specify a  
        function in place of the transition probabilities under different levels  
        of control.  
         
        Partially observed Markov decision processes can be modelled by  
        specifying a likelihood (as part of a generative model) and absorbing any  
        probabilistic mapping between hidden states and outcomes  
        into the transition probabilities G.  
         
        See also:spm_MDP, which uses multiple future states and a mean field  
        approximation for control states - but allows for different actions  
        at all times (as in control problems).  
         
        See also: spm_MDP_game_KL, which uses a very similar formulation but just  
        maximises the KL divergence between the posterior predictive distribution  
        over hidden states and those specified by preferences or prior beliefs.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_MDP_game_optimism.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_MDP_game_optimism", *args, **kwargs)
