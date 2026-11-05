from spm._runtime import Runtime


def DEM_sound_compression(*args, **kwargs):
    r"""
      Structure learning from sound files  
       __________________________________________________________________________  
         
        This routine illustrates the use of renormalizable generative models to  
        recognise, compress and generate sound files or auditory streams. This  
        application uses a blocking or grouping operator, which operates on the  
        neighbouring frequencies of a sonogram (i.e., time frequency  
        representation of a sound file). This means that local frequencies are  
        grouped together over time and assimilated using fast structure learning.  
         
        From the perspective of the generative model, the model generates  
        sequences of sequences that can be regarded as successively higher  
        abstractions or compositions of frequency glides. The ensuing generative  
        models can then generate sequences of sequences in a way that emulates  
        previous simulations of birdsong with hierarchically composed non-linear  
        dynamical (chaotic) systems but are generated in discrete state spaces  
        via the explicit representation of paths or trajectories.  
       __________________________________________________________________________  
        Copyright (C) 2019 Wellcome Trust Centre for Neuroimaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/DEM_sound_compression.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("DEM_sound_compression", *args, **kwargs)
