from spm._runtime import Runtime


def spm_set_costs(*args, **kwargs):
    r"""
      Sets prior preferences and costs MDP{n}.C{g} in a renormalising MDP  
        FORMAT MDP = spm_set_costs(MDP,S,chi)  
        MDP  - Generative model (hierarchical)  
        S    - list of modality streams; e.g. [2,3]  
        chi  - log prior for each modality; e.g., [-8,8]    
         
       --------------------------------------------------------------------------  
        This auxiliary routine generates outcomes at successive levels of a  
        renormalising generative model to identify rewarding or costly outcomes  
        at the lowest level, to set prior preferences or costs in MDP{n}.C{g}.  
        These priors are specified in terms of chi, the log probability. This  
        means a negative chi specifies a cost and a positive chi specifies a  
        reward in the respective streams.  
         
        Under these models,, a preferred or costly outcome corresponds to one or  
        more outcomes generated within each stream. This means that preferences  
        and costs are usually specified for distinct streams. In the example  
        above, stream 2 reports costly outcomes, while stream 3 reports preferred  
        outcomes.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_set_costs.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_set_costs", *args, **kwargs)
