from spm.__wrapper__ import Runtime


def spm_MDP_check(*args, **kwargs):
    """
      MDP structure checking  
        FORMAT [MDP] = spm_MDP_check(MDP)  
         
        MDP.V(T - 1,P,F)      - P allowable policies of T moves over F factors  
        or  
        MDP.U(1,P,F)          - P allowable actions at each move  
        MDP.T                 - number of outcomes  
         
        MDP.A{G}(O,N1,...,NF) - likelihood of O outcomes given hidden states  
        MDP.B{F}(NF,NF,MF)    - transitions among hidden under MF control states  
        MDP.C{G}(O,T)         - prior preferences over O outcomes in modality G  
        MDP.D{F}(NF,1)        - prior probabilities over initial states  
        MDP.E{F}(NF,1)        - prior probabilities over initial control  
         
        MDP.a{G}              - concentration parameters for A  
        MDP.b{F}              - concentration parameters for B  
        MDP.c{F}              - concentration parameters for C  
        MDP.d{F}              - concentration parameters for D  
        MDP.e{F}              - concentration parameters for E  
         
        optional:  
        MDP.s(F,T)            - vector of true states - for each hidden factor  
        MDP.o(G,T)            - vector of outcome     - for each outcome modality  
        MDP.u(F,T - 1)        - vector of action      - for each hidden factor  
        MDP.w(1,T)            - vector of precisions  
         
        if C or D are not specified, they will be set to default values (of no  
        preferences and uniform priors over initial steps).  If there are no  
        policies, it will be assumed that I = 1 and all policies (for each  
        marginal hidden state) are allowed.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_MDP_check.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_MDP_check", *args, **kwargs)
