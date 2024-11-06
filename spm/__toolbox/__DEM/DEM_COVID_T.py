from spm.__wrapper__ import Runtime


def DEM_COVID_T(*args, **kwargs):
    """
      FORMAT [DCM] = DEM_COVID_T  
         
        Demonstration of COVID-19 modelling using variational Laplace  
       __________________________________________________________________________  
         
        This demo routine focuses on surveillance and mitigation strategies in  
        the UK. It first estimate the parameters of a dynamic causal model for  
        the epidemic in the United Kingdom. Crucially, in this inversion the data  
        are supplemented with the total number of cases (in addition to positive  
        cases and daily deaths). It rests upon an augmented DCM that includes a  
        state of self isolation. Moving from a state of isolation depends upon a  
        negative test. Tracing and tracking in this model is reflected as a small  
        percentage of being tested if infected and asymptomatic. Otherwise, the  
        baseline testing is in play. We will consider the effects of changing  
        baseline testing and tracing and tracking at various phases of the  
        outbreak.  
         
        Finally, this routine performs a brief comparative analysis with Germany  
        to see if the differences with the UK can be explained in terms of  
        surveillance or clinical management.  
          
        NB: annotated notes appended to this routine illustrate a number of  
        analyses simulations relevant to various containment, suppression and  
        mitigation strategies. For example, the effect of early lockdowns, the  
        effect of maintaining a tracking and tracing policy at the inception of  
        the pandemic. In addition, there are notes showing how to incorporate  
        serological data during inversion of the dynamic causal model.  
       __________________________________________________________________________  
        Copyright (C) 2020 Wellcome Centre for Human Neuroimaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_COVID_T.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_COVID_T", *args, **kwargs)
