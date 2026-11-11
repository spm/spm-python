from spm._runtime import Runtime


def spm_MDP_generate(*args, **kwargs):
    r"""
      active inference and learning using belief propagation (factorised)  
        FORMAT [MDP] = spm_MDP_generate(MDP)  
         
        Input; MDP(m,n)       - structure array of m models over n epochs  
        MDP.U(1, Nf)          - controllable factors  
        MDP.V(Np,Nf)          - combinations of latent factors (policies)  
        MDP.T                 - number of time steps  
         
        MDP.A{Ng}(No(g),Ns(1),...,Ns(Nf)) - likelihood of outcomes, given hidden states  
        MDP.B{Nf}(Ns(f),Ns(f),Nu(f))      - transitions among states under control states  
        MDP.C{Ng}(No(g),1)    - prior probabilities over outcomes       (Dirichlet counts)  
        MDP.D{Nf}(Ns(f),1)    - prior probabilities over initial states (Dirichlet counts)  
        MDP.E{Nf}(Nu(f),1)    - prior probabilities over paths          (Dirichlet counts)  
        MDP.H{Nf}(Ns(f),1)    - prior probabilities over final states   (Dirichlet counts)  
         
        OPTIONS.A             - switch to evaluate explicit action  
         
        Outputs:  
        MDP.s(Nf,T)           - states   - for each hidden factor  
        MDP.o(Ng,T)           - outcomes - for each outcome modality  
        MDP.O{Ng,T}           - likelihoods   - for each outcome modality  
        MDP.u(Nu,T)           - controls - for each hidden factor  
         
        This routine provides solutions of active inference (minimisation of  
        variational free energy) using a generative model based upon a Markov  
        decision process. The model and inference scheme is formulated in  
        discrete space and time. This means that the generative model (and  
        process) are hidden Markov models whose dynamics are given by transition  
        probabilities among states and the likelihood corresponds to a particular  
        outcome conditioned upon hidden states.  
         
         
        See also: spm_MDP_VB_XXX, which is the corresponding variational message  
        passing scheme.  
       __________________________________________________________________________  
        Copyright (C) 2019 Wellcome Trust Centre for Neuroimaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_MDP_generate.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_MDP_generate", *args, **kwargs)
