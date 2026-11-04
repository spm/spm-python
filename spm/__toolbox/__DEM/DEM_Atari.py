from spm._runtime import Runtime


def DEM_Atari(*args, **kwargs):
    r"""
      Structure learning from pixels  
       __________________________________________________________________________  
         
        This routine addresses the problem of learning a generative model from  
        pixels, under the constraints supplied by sparse rewards. The problem is  
        solved in a fast and frugal way using a structure learning approach based  
        upon a generalised Markov decision process (that treats states and their  
        paths as pairs of random variables, whose dynamics are encoded in  
        transition tensors).  
          
        A key architectural aspect of these deep structures is an appeal to the  
        renormalisation group; in the sense that there is a recursive application  
        of grouping and reduction operators, as we move from one hierarchical  
        level to the next. These operate over both space and time: in the sense  
        that groups of pixels are jointly inferred over a short period of time;  
        such that the state any given level of the model generates the  
        instantaneous state and path (i.e., velocity) of a group of latent states  
        at the lower level. In these examples, the group operator effectively  
        tiles a lattice of latent states (and instantaneous paths) into little  
        contiguous squares. This necessary induces a separation of temporal  
        scales such as the states at the highest level see all the pixels at the  
        lowest level and, effectively,, encode a trajectory over to the 2^n  
        timesteps, where n is the depth of the model.  
          
        Note that in this illustration, there is no learning of model parameters.  
        The structure is identified using a simple form of supervised structure  
        learning. This simple form conforms to the approach in machine learning,  
        in which random play is sporadically rewarded. By selecting episodes of  
        play (i.e., exemplar training data) that end with a reward, one can  
        emulate reinforcement learning with active model selection. This can be  
        read as replacing a scheme in which 'everything is presented but rewarded  
        sequences are learned' with the equivalent protocol in which 'rewarded  
        sequences are presented and everything is learned'. The resulting  
        structure is then sufficient to reproduce expert play; because this is  
        the kind of play that the model knows.  
          
        One can finesse expert play by the use of inductive inference; provided  
        initial conditions or novel trajectories to be recognised as such, and  
        actively reconfigured to recognisable (expert trajectories) through  
        explicit action. Explicit action refers to (merely) reflexive active  
        inference; namely, selecting those actions that minimise free energy that  
        produce outcomes that match predicted outcomes. Here, the outcomes are  
        pixel-based outcomes.  
       __________________________________________________________________________  
        Copyright (C) 2019 Wellcome Trust Centre for Neuroimaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/DEM_Atari.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("DEM_Atari", *args, **kwargs)
