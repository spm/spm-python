from spm._runtime import Runtime


def spm_MDP_structure_learning(*args, **kwargs):
    r"""
      structure learning of factorised Markov decision processes  
        FORMAT mdp = spm_MDP_structure_learning(mdp,O,[OPTIONS])  
         
        mdp.p - initial Dirichlet counts [1/32]  
        mdp.q - precise Dirichlet counts [512]  
        O     - probabilitic exemplars of paths  
         
        OPTIONS.N  [0]   - suppress neuronal responses  
        OPTIONS.P  [0]   - suppress plotting  
        OPTIONS.G  [1]   - suppress graphics  
        OPTIONS.B  [1]      - replay  
         
        OPTIONS.NF [4]   - maxmium number of factors  
        OPTIONS.NS [32,...] - maxmium number of states  
        OPTIONS.NU [16,...] - maxmium number of paths  
        OPTIONS.UB [1]      - model prior: bound on Ns  
         
        mdp   - generative model: with mdp.a, mdp.b  
         
        This routine returns a generative model (mdp) in the form of an MDP,  
        given a sequence of outcomes. If the outcomes are not available, then  
        they can be generated automatically from a generative process, specified  
        with an MDP structure (see spm_MDP_structure_teaching). The generative  
        model learns from successive epochs of data generated under the first  
        level of each factor of the process. By exploring different extensions to  
        the model (using Bayesian model comparison) successive epochs are  
        assimilated under a model structure that accommodates paths. This routine  
        makes certain assumptions about the structural form of generative models  
        at any given level of a hierarchical model. These are minimal  
        assumptions:  
          
        (i) Dynamics are conditionally independent of outcomes. This means that  
        the generative model can be factorised into a likelihood mapping (A) and  
        transition probabilities over latent states (B)  
          
        (ii) Latent states can be partitioned into factors, whose dynamics are  
        conditionally independent   
          
        (iii) The dynamics for each factor can be partitioned into discrete  
        paths.  
          
        This leads to a generic form for any level of a hierarchical (deep)  
        Markov decision process in which the likelihood mapping (for each  
        modality) is a tensor whose trailing dimensions correspond to the  
        dimensions of each factor. The (transition) priors are tensors, with a  
        probability transition matrix for each path. In addition, the initial  
        state and path of each factor are specified with D and E. With this form,  
        structure learning can simply consider the addition of a latent state, a  
        latent path or a new factor.  
          
        It is assumed that the first path of any factor has no dynamics and  
        corresponds to an identity operator. Subsequent paths can have any form.  
        Because outcomes are assumed to be generated under the first level of  
        each factor, they generate the same outcome. In other words, the  
        likelihood mapping is shared by the first state of every factor. In turn,  
        this means that adding a factor entails adding a second state to the  
        implicit first state of the new factor.  
         
        See: spm_MDP_log_evidence.m, spm_MDP_VB_update and spm_MDP_VB_sleep.m  
             spm_MDP_structure_teaching.m  
       __________________________________________________________________________  
        Copyright (C) 2005 Wellcome Trust Centre for Neuroimaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_MDP_structure_learning.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_MDP_structure_learning", *args, **kwargs)
