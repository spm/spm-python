from spm.__wrapper__ import Runtime


def DEM_demo_fMRI_PEB(*args, **kwargs):
    """
      Demonstration of PEB for multisession spectral DCM studies  
       __________________________________________________________________________  
        This demonstration routine illustrates the analysis of a multisession  
        fMRI study using spectral DCM. Crucially, the between session effects are  
        characterised using empirical Bayes and Bayesian model reduction. This  
        means that the original session data are only inverted once (at the  
        within session level). The resulting posterior estimates and then used to  
        make inferences about between session effects (e.g., time or drug  
        effects). The basic question addressed in this sort of analysis is where  
        between session effects are expressed in terms of connectivity or  
        parameters of neuronal fluctuations. These sorts of effects are specified  
        in a second level design matrix in the usual way and can be identified  
        using Bayesian model reduction.  
         
        in this example, we analyse three sessions with a monotonic change in the  
        intrinsic (self) connectivity over three sessions. This involves  
        decreases in diagonal A parameters at the first two levels of a simple  
        three node hierarchy - and an increase at the highest (third) level.  
        Physiologically, this corresponds to a decrease in self-inhibition (or  
        increase in excitability) in the lower notes for regions, as time goes  
        on.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_demo_fMRI_PEB.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_demo_fMRI_PEB", *args, **kwargs, nargout=0)
