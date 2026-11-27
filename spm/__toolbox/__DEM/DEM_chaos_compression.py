from spm._runtime import Runtime


def DEM_chaos_compression(*args, **kwargs):
    r"""
      Structure learning from pixels: the Lorenz attractor  
       __________________________________________________________________________  
         
        This demonstration routine uses a renormalisable generative model to  
        learn, recognise and generate stochastic chaos. It uses the same  
        procedures used to learn paths and orbits from image sequences, apt for  
        video compression. Effectively, it learns stochastic chaos based upon  
        exponential divergence of trajectories in terms of a switching dynamical  
        system, where successive paths are selected based upon a probability  
        transition matrix. Here, an image of a white ball moving on the  
        attracting manifold of a Lorenz system is generated. This is then  
        quantised and learned in the usual way by fast structure learning.  
        Subsequent (active) learning then fills in probability transitions, which  
        are subsequently refined using (simple) Bayesian model reduction. The  
        ensuing generative model can then be used to filter images (i.e.,  
        recognise the phase of the underlying dynamics), and generate stochastic  
        chaos when the stimulus is removed.  
       __________________________________________________________________________  
        Copyright (C) 2019 Wellcome Trust Centre for Neuroimaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/DEM_chaos_compression.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("DEM_chaos_compression", *args, **kwargs)
