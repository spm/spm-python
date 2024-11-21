from spm.__wrapper__ import Runtime


def DEM_demo_texture(*args, **kwargs):
    """
      This demonstration considers the figure-ground segregation problem where,   
        crucially, a figure is defined texturally - in terms of its second order   
        statistics; in other words, a visual object is manifest in terms of its   
        texture or spectral power density in the spatial domain. This definition   
        precludes any first-order attributes; such as increased luminance. This   
        sort of problem is common in the inverse literature and is usually solved   
        using a prior on the [co]variance of random fluctuations generating data.   
        Here, we simulate a contiguous object, whose texture is determined by the   
        variance of random fluctuations in luminance - and the variance (or   
        precision) is modulated by Gaussian basis functions. The resulting signal   
        is mixed with uniform Gaussian noise to produce sensory data. These   
        (one-dimensional) data are then subject to Bayesian inversion using   
        generalized predictive coding - (as implemented in spm_LAP) - to recover   
        the underlying object.  
          
        Technically, this scheme optimizes expectations of the hidden causes of   
        the data, which are the amplitude of radial basis functions controlling   
        the precision of retinotopic signals. Heuristically, the figure is   
        recognized by selectively attending to sensory input from the figure.   
        This enables sensory noise to be suppressed in unattended parts of the   
        visual field. However, this form of attention is distinct from simply   
        boosting sensory precision (the precision of sensory prediction errors)   
        as in simulations of the Posner paradigm or biased competition. Here,   
        the hidden causes are optimized in a way that renders them less precise   
        and therefore more sensitive to ascending (prediction error) sensory   
        input. This illustrates the functional importance of the relative   
        precision of sensory and extrasensory prediction errors in modulating   
        the influence of ascending sensory information that competes to influence   
        posterior expectations.  
         
        PS: for a 2-D simulation delete 'return' below.  
         
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_demo_texture.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_demo_texture", *args, **kwargs)
