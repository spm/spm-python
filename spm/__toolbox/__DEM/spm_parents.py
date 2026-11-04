from spm._runtime import Runtime


def spm_parents(*args, **kwargs):
    r"""
      Returns parents and children of MDP likelihood mappings  
        FORMAT [j,i] = spm_parents(id,g,Q)  
          
        id - identifier or index structure  
         id.A{g} List of parents  of A{g}  
         
         id.ff - List of domain factors  
         id.fg - List of parents  of A{g} under each combination of domains   
         id.gg - List of children of A{g} under each combination of domains  
          
        g  - index of likelihood mapping A{g}  
        Q  - posterior over domain factors (id.ff) (or states)  
         
        j  -   domain of A{g}: hidden factors     (i.e., parents)  
        i  - codomain of A{g}: outcome modalities (i.e., children)  
         
        Returns the domain [codomains] of factors [modalities] for this  
        likelihood mapping. These [co] domains may or may not be state-dependent.  
        If they are state-dependent, the maximum a posteriori [co] domain is  
        returned.  
         
        domains (parents or 'cause') and co-domains (children or 'effect')  
       ==========================================================================  
        id.A - cell array of parents of A factors at the same level  
        id.B - cell array of parents of B factors at the same level  
        id.C - cell array of parents of C priors  at the same level  
        id.D - cell array of parents of initial state at next level  
        id.E - cell array of parents of initial paths at next level  
         
        id.ff   - List of domain factors  
        id.fg   - List of parents  of A{g} under each combination of domains   
        id.gg   - List of children of A{g} under each combination of domains  
         
        id.g{k} - Partition of selected (i.e., attended) children of A{g}  
        id.ge   - Indices of outcomes subtending expected free energy  
         
        id.fu   - List of factors with contolled paths  
        id.fp   - List of factors with inferred  paths   
         
        see: spm_MDP_VB_XXX.m  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_parents.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_parents", *args, **kwargs)
