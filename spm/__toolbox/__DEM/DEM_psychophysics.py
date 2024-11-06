from spm.__wrapper__ import Runtime


def DEM_psychophysics(*args, **kwargs):
    """
      FORMAT DCM = DEM_psychophysics  
         
        Demonstration of psychometric curve fitting and model comparison  
       __________________________________________________________________________  
         
        This demonstration routine illustrates the fitting of psychometric  
        functions under different models or hypotheses. The models in question  
        are specified by various constraints on the model parameters; namely,  
        changes in bias and sensitivity. The generative model uses a binomial  
        likelihood function and a logistic function for the predicted  
        psychometric curves.  
          
        A binomial likelihood model means that (under the assumption of a large  
        number of trials) following a (variance stabilising) square root  
        transform, the error variance of the number of correct responses is  
        unity. If we scale the number of correct responses to reflect the  
        proportion of correct responses, then the precision of the ensuing  
        (square root transform) data feature is the total number of responses.  
        This provides a simple and efficient way to specify the generative model  
        as a generalised linear model, based upon a standard logistic function,  
        whose parameters correspond to bias and sensitivity.  
          
        In this example, data are loaded from a CSV file and converted into the  
        proportion of correct responses, under two levels or conditions of an  
        experimental factor (baseline and blindspot). The generative model is  
        equipped with parameters corresponding to changes in bias and  
        sensitivity. Crucially, these changes have parity; namely, increases and  
        decreases. This means that there are, potentially, eight models:  
        corresponding to the presence or absence of an increase or decrease in  
        bias and sensitivity. In the example below, three of these models are  
        compared, in terms of their marginal likelihood (as approximated by a  
        softmax function of the ensuing variational free energy).  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_psychophysics.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_psychophysics", *args, **kwargs)
