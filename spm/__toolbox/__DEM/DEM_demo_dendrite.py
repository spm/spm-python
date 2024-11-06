from spm.__wrapper__ import Runtime


def DEM_demo_dendrite(*args, **kwargs):
    """
      Free-energy and the single neuron:  
       __________________________________________________________________________  
        This demo illustrates the use of Lotka-Volterra form SHCs (Stable  
        heteroclinic channels) to prescribe active sampling (inference). In this  
        example, we assume that neurons self-organise to minimise a free energy  
        bound on the informational surprise in the pre-synaptic inputs that are   
        sampled.  We model this as a selective pruning of post-synaptic spines   
        that are expressed on the dendritic tree.  This pruning occurs when the   
        (optimised) post-synaptic gain falls to small values.  Crucially, post-  
        synaptic gain (encoding the precision of the neuron's prediction errors   
        about its pre-synaptic inputs) is itself optimised with respect to free-  
        energy.  Furthermore, the pruning itself suppresses free-energy as the   
        neuron selects post-synaptic specialisations that conform to its   
        expectations.  This provide a principled account of how neurons organise   
        and selectively sample the myriad of potential pre-synaptic inputs they   
        are exposed to, but it also connects elemental neuronal (dendritic)   
        processing to generic schemes in statistics and machine learning:  
        such as Bayesian model selection and automatic relevance determination.   
        The demonstration of this scheme simulates direction selectivity in post  
        synaptic transients and (see notes after 'return') spike-timing dependent  
        plasticity.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_demo_dendrite.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_demo_dendrite", *args, **kwargs, nargout=0)
