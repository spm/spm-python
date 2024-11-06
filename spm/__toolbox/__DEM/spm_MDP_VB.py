from spm.__wrapper__ import Runtime


def spm_MDP_VB(*args, **kwargs):
    """
      active inference and learning using variational Bayes  
        FORMAT [MDP] = spm_MDP_VB(MDP,OPTIONS)  
         
        MDP.S(N,1)        - true initial state  
        MDP.V(T - 1,P)    - P allowable policies (control sequences)  
         
        MDP.A(O,N)        - likelihood of O outcomes given N hidden states  
        MDP.B{M}(N,N)     - transition probabilities among hidden states (priors)  
        MDP.C(N,1)        - prior preferences   (prior over future outcomes)  
        MDP.D(N,1)        - prior probabilities (prior over initial states)  
         
        MDP.a(O,N)        - concentration parameters for A  
        MDP.b{M}(N,N)     - concentration parameters for B  
        MDP.c(N,N)        - concentration parameters for habitual B  
        MDP.d(N,1)        - concentration parameters for D  
        MDP.e(P,1)        - concentration parameters for u  
         
        optional:  
        MDP.s(1,T)        - vector of true states  
        MDP.o(1,T)        - vector of observations   
        MDP.u(1,T)        - vector of actions  
        MDP.w(1,T)        - vector of precisions  
         
        MDP.alpha         - upper bound on precision (Gamma hyperprior - shape [1])  
        MDP.beta          - precision over precision (Gamma hyperprior - rate  [1])  
         
        OPTIONS.plot      - switch to suppress graphics: (default: [0])  
        OPTIONS.scheme    - {'Free Energy' | 'KL Control' | 'Expected Utility'};  
        OPTIONS.habit     - switch to suppress habit learning: (default: [1])  
         
         
        produces:  
         
        MDP.P(M,T)        - probability of emitting action 1,...,M at time 1,...,T  
        MDP.Q(N,T)        - an array of conditional (posterior) expectations over  
                                N hidden states and time 1,...,T  
        MDP.X             - and Bayesian model averages over policies  
        MDP.R             - conditional expectations over policies  
         
        MDP.un            - simulated neuronal encoding of hidden states  
        MDP.xn            - simulated neuronal encoding of policies  
        MDP.wn            - simulated neuronal encoding of precision (tonic)  
        MDP.dn            - simulated dopamine responses (phasic)  
        MDP.rt            - simulated reaction times  
         
        This routine provides solutions of an active inference scheme  
        (minimisation of variational free energy) using a generative model based  
        upon a Markov decision process. This model and inference scheme is  
        formulated in discrete space and time. This means that the generative  
        model and process are finite state machines or hidden Markov models,  
        whose dynamics are given by transition probabilities among states - and  
        the likelihood corresponds to the probability of an outcome given hidden  
        states. For simplicity, this routine assumes that action (the world) and  
        hidden control states (in the model) are isomorphic.   
         
        This implementation equips agents with the prior beliefs that they will  
        maximise expected free energy: expected free energy is the free energy of  
        future outcomes under the posterior predictive distribution. This can be  
        interpreted in several ways - most intuitively as minimising the KL  
        divergence between predicted and preferred outcomes (specified as prior  
        beliefs) - while simultaneously minimising the (predicted) entropy of  
        outcomes conditioned upon hidden states. Expected free energy therefore  
        combines KL optimality based upon preferences or utility functions with  
        epistemic value or information gain.  
         
        This particular scheme is designed for any allowable policies or control  
        sequences specified in MDP.V. Constraints on allowable policies can limit  
        the numerics or combinatorics considerably. For example, situations in  
        which one action can be selected at one time can be reduced to T polices  
        - with one (shift) control being emitted at all possible time points.  
        This specification of polices simplifies the generative model, allowing a  
        fairly exhaustive model of potential outcomes - eschewing a mean field  
        approximation over successive control states. In brief, the agent encodes  
        beliefs about hidden states in the past and in the future conditioned on  
        each policy (and a non-sequential state-state policy called a habit).  
        These conditional expectations are used to evaluate the (path integral)  
        of free energy that then determines the prior over policies. This prior  
        is used to create a predictive distribution over outcomes, which  
        specifies the next action.  
         
        In addition to state estimation and policy selection, the scheme also  
        updates model parameters; including the state transition matrices,  
        mapping to outcomes and the initial state. This is useful for learning  
        the context. In addition, by observing its own behaviour, the agent will  
        automatically learn habits. Finally, by observing policies chosen over  
        trials, the agent develops prior expectations or beliefs about what it  
        will do. If these priors (over policies - that include the habit) render  
        some policies unlikely (using an Ockham's window), they will not be  
        evaluated.  
         
        See also:spm_MDP, which uses multiple future states and a mean field  
        approximation for control states - but allows for different actions  
        at all times (as in control problems).  
         
        See also: spm_MDP_game_KL, which uses a very similar formulation but just  
        maximises the KL divergence between the posterior predictive distribution  
        over hidden states and those specified by preferences or prior beliefs.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_MDP_VB.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_MDP_VB", *args, **kwargs)
