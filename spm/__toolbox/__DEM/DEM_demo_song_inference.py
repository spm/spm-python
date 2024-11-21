from spm.__wrapper__ import Runtime


def DEM_demo_song_inference(*args, **kwargs):
    """
      Perceptual categorisation of bird songs: The generative model of   
        birdsong used in this simulation comprises a Lorenz attractor with two   
        control parameters (or hidden causes), which, in turn, delivers two   
        control parameters to a synthetic syrinx to produce 'chirps' that are   
        modulated in amplitude and frequency.  The chirps were then presented   
        as a stimulus to a synthetic bird to see if it could infer the   
        underlying causal states and thereby categorise the song. This entails   
        minimising free energy by changing the internal representation of the   
        control parameters. Each simulated song comprises a series of chirps   
        whose frequency and number fall progressively from song a to song c,   
        as a causal state (known as the Raleigh number) is decreased.  The   
        simulations show that the causes are identified after about 600   
        milliseconds with high conditional precision (90% confidence intervals   
        are shown in grey). These simulations illustrate the nature of   
        perceptual categorisation under generalised predictive coding: Here,   
        recognition corresponds to mapping from a continuously changing and   
        chaotic sensory input to a fixed point in perceptual space.  
         
        The various bird songs can be played by right clicking on the sonogram  
        images, after the routine has completed.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_demo_song_inference.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_demo_song_inference", *args, **kwargs, nargout=0)
