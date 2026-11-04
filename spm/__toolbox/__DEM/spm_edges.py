from spm._runtime import Runtime


def spm_edges(*args, **kwargs):
    r"""
      Returns parents and children of MDP likelihood mapping  
        FORMAT [j,i,q] = spm_edges(id,g,Q)  
          
        id - identifier or index structure  
         id.A{g} State-independent domain  
         
         id.ff - List of domain factors  
         id.fg - List of parents  for A{g} under each combination of domains   
         id.gg - List of children for A{g} under each combination of domains  
          
        g  - index of likelihood mapping A{g}  
        Q  - posterior over domain factors (id.ff)  
         
        j{}  -  parents of A{g}: hidden factors  
        i{}  - children of A{g}: outcome modalities  
        q    - posterior over parents and children  
         
        Returns the domain [codomains] of factors [modalities] for this  
        likelihood mapping. These [co] domains may or may not be state-dependent.  
        If they are state-dependent, the posteriors are returned.  
       __________________________________________________________________________  
                    
        id.A{g} - Indices of parents of A{g}  
        id.D{f} - Indices of parents of initial states of factor B{f}  
        id.E{f} - Indices of parents of paths of factor B{f}   
         
        id.ff   - List of domain factors  
        id.fg   - List of parents  of A{g} under each combination of domains   
        id.gg   - List of children of A{g} under each combination of domains  
         
        id.g{k} - Partition of selected (i.e., attended) children of A{g}  
        id.ge   - Indices of outcomes subtending expected free energy  
         
        id.fu   - List of factors with contolled paths  
        id.fp   - List of factors with inferred  paths   
         
        see: spm_parents.m  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_edges.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_edges", *args, **kwargs)
