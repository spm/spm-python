from spm.__wrapper__ import Runtime


def spm_MDP_VB_X(*args, **kwargs):
    """
      active inference and learning using variational message passing  
        FORMAT [MDP] = spm_MDP_VB_X(MDP,OPTIONS)  
         
        Input; MDP(m,n)       - structure array of m models over n epochs  
         
        MDP.V(T - 1,P,F)      - P allowable policies (T - 1 moves) over F factors  
        or  
        MDP.U(1,P,F)          - P allowable actions at each move  
        MDP.T                 - number of outcomes  
         
        MDP.A{G}(O,N1,...,NF) - likelihood of O outcomes given hidden states  
        MDP.B{F}(NF,NF,MF)    - transitions among states under MF control states  
        MDP.C{G}(O,T)         - (log) prior preferences for outcomes (modality G)  
        MDP.D{F}(NF,1)        - prior probabilities over initial states  
        MDP.E(P,1)            - prior probabilities over policies  
         
        MDP.a{G}              - concentration parameters for A  
        MDP.b{F}              - concentration parameters for B  
        MDP.c{G}              - concentration parameters for C  
        MDP.d{F}              - concentration parameters for D  
        MDP.e                 - concentration parameters for E  
         
        optional:  
        MDP.s(F,T)            - matrix of true states - for each hidden factor  
        MDP.o(G,T)            - matrix of outcomes    - for each outcome modality  
        or .O{G}(O,T)         - likelihood matrix     - for each outcome modality  
        MDP.u(F,T - 1)        - vector of actions     - for each hidden factor  
         
        MDP.alpha             - precision - action selection [512]  
        MDP.lambda            - precision - action selection (likelihood) [512]  
        MDP.beta              - precision over precision (Gamma hyperprior - [1])  
        MDP.chi               - Occams window for deep updates  
        MDP.tau               - time constant for gradient descent [4]  
        MDP.eta               - learning rate for model parameters  
        MDP.zeta              - Occam's window for polcies [3]  
        MDP.erp               - resetting of initial states, to simulate ERPs [4]  
         
        MDP.demi.C            - Mixed model: cell array of true causes (DEM.C)  
        MDP.demi.U            - Bayesian model average (DEM.U) see: spm_MDP_DEM  
        MDP.link              - link array to generate outcomes from  
                                subordinate MDP; for deep (hierarchical) models  
         
        OPTIONS.plot          - switch to suppress graphics:  (default: [0])  
        OPTIONS.gamma         - switch to suppress precision: (default: [0])  
        OPTIONS.D             - switch to update initial states over epochs  
        OPTIONS.BMR           - Bayesian model reduction for multiple trials  
                                see: spm_MDP_VB_sleep(MDP,BMR)  
        Outputs:  
         
        MDP.P(M1,...,MF,T)    - probability of emitting action M1,.. over time  
        MDP.Q{F}(NF,T,P)      - expected hidden states under each policy  
        MDP.X{F}(NF,T)        - and Bayesian model averages over policies  
        MDP.R(P,T)            - response: conditional expectations over policies  
         
        MDP.un          - simulated neuronal encoding of hidden states  
        MDP.vn          - simulated neuronal prediction error  
        MDP.xn          - simulated neuronal encoding of policies  
        MDP.wn          - simulated neuronal encoding of precision (tonic)  
        MDP.dn          - simulated dopamine responses (phasic)  
        MDP.rt          - simulated reaction times  
         
        MDP.F           - (P x T) (negative) free energies over time  
        MDP.G           - (P x T) (negative) expected free energies over time  
        MDP.H           - (1 x T) (negative) total free energy over time  
        MDP.Fa          - (1 x 1) (negative) free energy of parameters (a)  
        MDP.Fb          - ...  
         
        This routine provides solutions of active inference (minimisation of  
        variational free energy) using a generative model based upon a Markov  
        decision process (or hidden Markov model, in the absence of action). The  
        model and inference scheme is formulated in discrete space and time. This  
        means that the generative model (and process) are  finite state machines  
        or hidden Markov models whose dynamics are given by transition  
        probabilities among states and the likelihood corresponds to a particular  
        outcome conditioned upon hidden states.  
         
        When supplied with outcomes, in terms of their likelihood (O) in the  
        absence of any policy specification, this scheme will use variational  
        message passing to optimise expectations about latent or hidden states  
        (and likelihood (A) and prior (B) probabilities). In other words, it will  
        invert a hidden Markov model. When  called with policies, it will  
        generate outcomes that are used to infer optimal policies for active  
        inference.  
         
        This implementation equips agents with the prior beliefs that they will  
        maximise expected free energy: expected free energy is the free energy of  
        future outcomes under the posterior predictive distribution. This can be  
        interpreted in several ways - most intuitively as minimising the KL  
        divergence between predicted and preferred outcomes (specified as prior  
        beliefs) - while simultaneously minimising ambiguity.  
         
        This particular scheme is designed for any allowable policies or control  
        sequences specified in MDP.V. Constraints on allowable policies can limit  
        the numerics or combinatorics considerably. Further, the outcome space  
        and hidden states can be defined in terms of factors; corresponding to  
        sensory modalities and (functionally) segregated representations,  
        respectively. This means, for each factor or subset of hidden states  
        there are corresponding control states that determine the transition  
        probabilities.  
         
        This specification simplifies the generative model, allowing a fairly  
        exhaustive model of potential outcomes. In brief, the agent encodes  
        beliefs about hidden states in the past (and in the future) conditioned  
        on each policy. The conditional expectations determine the (path  
        integral) of free energy that then determines the prior over policies.  
        This prior is used to create a predictive distribution over outcomes,  
        which specifies the next action.  
         
        In addition to state estimation and policy selection, the scheme also  
        updates model parameters; including the state transition matrices,  
        mapping to outcomes and the initial state. This is useful for learning  
        the context. Likelihood and prior probabilities can be specified in terms  
        of concentration parameters (of a Dirichlet distribution (a,b,c,..). If  
        the corresponding (A,B,C,..) are supplied, they will be used to generate  
        outcomes; unless called without policies (in hidden Markov model mode).  
        In this case, the (A,B,C,..) are treated as posterior estimates.  
         
        If supplied with a structure array, this routine will automatically step  
        through the implicit sequence of epochs (implicit in the number of  
        columns of the array). If the array has multiple rows, each row will be  
        treated as a separate model or agent. This enables agents to communicate  
        through acting upon a common set of hidden factors, or indeed sharing the  
        same outcomes.  
         
        See also: spm_MDP, which uses multiple future states and a mean field  
        approximation for control states - but allows for different actions at  
        all times (as in control problems).  
         
        See also: spm_MDP_game_KL, which uses a very similar formulation but just  
        maximises the KL divergence between the posterior predictive distribution  
        over hidden states and those specified by preferences or prior beliefs.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_MDP_VB_X.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_MDP_VB_X", *args, **kwargs)
