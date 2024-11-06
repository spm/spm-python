from spm.__wrapper__ import Runtime


def DEM_demo_fMRI_HMM(*args, **kwargs):
    """
      Demonstration of Hidden Markov models for fMRI  
       __________________________________________________________________________  
         This demonstration routine illustrates the modelling of state  
         transitions generating resting state fMRI timeseries. The hidden states  
         are modelled as a hidden Markov model, where each state corresponds to a  
         particular  point in the parameter space of effective connectivity. This  
         effective connectivity then generates complex cross spectral data  
         features  of the observed timeseries. Model specification requires prior  
         constraints on the probability transition matrix among hidden states,  
         which implicitly specifies the number of hidden states. The user also  
         has to specify the number of windows for epochs to apply to the  
         timeseries, where each epoch  places a lower bound on the duration of  
         each (discrete) state.  
            We first generate synthetic data using regular transitions among  
         three hidden states  (C.F., a discrete version of a heteroclinic  
         cycle  for orbit). The data are then converted by a routine that  
         combines a parametric empirical Bayesian model and a hidden Markov model  
         (as implemented as a special case of a Markov decision process). This  
         inversion is repeated for each model specified in terms of the  
         transition matrices (as prior Dirichlet concentration parameters).  
         Setting a prior transition parameter to 0 precludes that transition. In  
         this way, several different models of transitions and number of hidden  
         states can be  scored in terms of  the variational free energy.  
            Following inversion, the results are plotted in terms of expected  
         state transitions, fluctuations in connections that are allowed to  
         change (specified in the usual way by DCM.b), the deviations in  
         connectivity associated with each hidden state and the expected  
         probability transition matrix.  
            Finally, we consider Bayesian model comparison in terms of group  
         differences (here, simply the difference between the first and second  
         simulated subject).  Bayesian model comparison is simple to do in this  
         context  by comparing the free energy of a hidden Markov model in which  
         both groups share the same state dependent connections and transition  
         probabilities, with two independent models. These can be evaluated  
         efficiently using Bayesian model reduction implicit in PEB. in this  
         example, we did not introduce any differences between the two groups  
         (i.e., subjects) and therefore expected to infer no group effect.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_demo_fMRI_HMM.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_demo_fMRI_HMM", *args, **kwargs, nargout=0)
