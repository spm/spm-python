from spm.__wrapper__ import Runtime


def DEM_dSprites(*args, **kwargs):
    """
      Demo of active inference and structure learning (i.e.,disentanglement)  
       __________________________________________________________________________  
         
        This routine uses a Markov decision process formulation of active  
        inference to illustrate structure learning. Structure learning here is  
        read as optimising the structure of a generative model that, crucially,  
        includes dynamics. This foregrounds the sequential order and temporal  
        scheduling of various updates. In this example, we start with a simple  
        problem in which one or more objects can be removed around in a  
        two-dimensional space. The kind of structure learning considered here can  
        be likened to nonparametric Bayes; namely, the addition of a model  
        component if licensed in terms of model evidence or marginal likelihood.  
        Procedurally, this means that with each new stimulus (sequence of  
        observations) various models are compared that entail the addition of a  
        new latent state, path or factor. If the ELBO (i.e., negative variational  
        free energy) increases the addition is accepted but not otherwise. The  
        training sequences are carefully constructed to reflect the ordinal  
        structure of observations. In other words, structure learning is  
        predicated on both the content and dynamics of the generative process.  
          
        This demonstration calls a belief propagation scheme with factorisation  
        of latent states into factors. Furthermore, the likelihood mapping is  
        factorised into conditionally independent outcome modalities. This means  
        that the size of any requisite tensor for belief updating is upper  
        bounded by the factorisation or mean field approximation). This mitigates  
        the van Neumann bottleneck; leading to increased efficiency at all three  
        levels of optimisation (inference, learning and model selection).  
          
        A key aspect of this demonstration routine is that it deals with discrete  
        state space generative models (and observations). This means that belief  
        propagation and updating can be implemented using linear (tensor)  
        operators; without worrying about nonlinearities of the sort found in  
        continuous state space models.  
         
       _________________________________________________________________________  
        Copyright (C) 2019 Wellcome Trust Centre for Neuroimaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_dSprites.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_dSprites", *args, **kwargs)
