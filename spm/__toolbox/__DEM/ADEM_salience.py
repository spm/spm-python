from spm.__wrapper__ import Runtime


def ADEM_salience(*args, **kwargs):
    """
      Saccadic eye movements under active inference  
       __________________________________________________________________________  
        This demo illustrates exploration or visual search in terms of optimality  
        principles based on straightforward ergodic or allostatic principles.  
        In other words, to maintain the constancy of our external milieu, it is  
        sufficient to expose ourselves to predicted and predictable stimuli.  
        Being able to predict what is currently seen also enables us to predict  
        fictive sensations that we will experience from another viewpoint. This  
        provides a principled way in which to explore and sample the world for  
        example with visual searches using saccadic eye movements. These  
        theoretical considerations are remarkably consistent with a number  
        of compelling heuristics; most notably the Infomax principle or the  
        principle of minimum redundancy, signal detection theory and recent  
        formulations of salience in terms of Bayesian surprise. The example  
        here uses saliency (the posterior precision associated with fictive  
        sampling of sensory data) to simulate saccadic eye movements under  
        active inference.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/ADEM_salience.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ADEM_salience", *args, **kwargs, nargout=0)
