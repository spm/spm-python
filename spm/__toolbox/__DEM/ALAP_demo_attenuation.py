from spm.__wrapper__ import Runtime


def ALAP_demo_attenuation(*args, **kwargs):
    """
      This demonstration illustrates context or state-dependent precision (i.e.  
        attention), which is necessary to disambiguate between sensations  
        caused exogenously and self-generated sensations. In brief, it is  
        necessary to attend away from the sensory consequences of action to  
        preclude sensory evidence overriding the prior beliefs that cause  
        movement. This necessarily reduced the confidence in self-generated  
        sensations and provides a simple (Bayes-optimal) explanation for sensory  
        attenuation - in terms of the attention of sensory precision. We  
        illustrate this in the setting of the force matching illusion and go on  
        to show that increasing the conviction in (precision of) prior beliefs  
        abolishes sensory attenuation at the expense of false (delusional)   
        posterior beliefs about antagonistic external forces.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/ALAP_demo_attenuation.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ALAP_demo_attenuation", *args, **kwargs, nargout=0)
