from spm.__wrapper__ import Runtime


def ADEM_cost_SHC(*args, **kwargs):
    """
      This demo illustrates the use of priors on the motion of hidden states as  
        polices. It simulates exploration and exploitation using radial basis  
        function attractors and auto-vitiative (self-destroying) attractors  
        as the basis of the prior. These dynamics enforce exploration, under  
        active inference. In turn, this exploration enables perceptual learning  
        to associate attractors with changes in physiological states (cf,  
        rewards). This can be exploited to by formal priors to ensure regions of  
        physiological state-space are avoided.  
        We look at this scheme using simulated pathology; first, we simulate a  
        (neurodegenerative) reduction in log-precision (cf Parkinson's disease) on  
        the motion of physical states.  This results in active inference with  
        a loss of precise volitional movement and subsequent failure to optimise   
        physiological states. Second, we look at the effects of precision on   
        learning by increasing log-precision (cf, Addition) on the motion of  
        physiological states. This results in a failure to learn and, again,   
        subsequent failure to optimise physiological states.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/ADEM_cost_SHC.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ADEM_cost_SHC", *args, **kwargs, nargout=0)
