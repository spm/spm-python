from spm.__wrapper__ import Runtime


def MDP_DEM_Mixed_Models_Movement(*args, **kwargs):
    """
      This demo illustrates a series of computational pathologies as elicited  
        during a synthetic neurological examination. This focuses upon an  
        examination of the biceps reflex, and a simple coordination task. Each of  
        these are simulated for an arm that may move in three dimensions through  
        internal and external rotation of the shoulder, flexion and extension of  
        the shoulder, and flexion and extension of the elbow. These dynamics play  
        out through an active Bayesian filtering scheme, where a series of  
        attracting points draw the hand to different locations in 3D space. The  
        selection of these attracting points involves a hierarhical Markov  
        Decision Process, which identifies these sequences based upon the prior  
        belief that (1) the sequence will minimise expected free energy and (2)  
        the sequence is consistent with the trajectory predicted by the highest  
        (contextual) level of the model.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/MDP_DEM_Mixed_Models_Movement.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("MDP_DEM_Mixed_Models_Movement", *args, **kwargs, nargout=0)
