from spm._runtime import Runtime


def DEM_AtariII(*args, **kwargs):
    r"""
      Structure learning from pixels  
       __________________________________________________________________________  
         
        This version of the Atari demos illustrates the use of multimodal streams  
        in a renormalising generative model. The first stream derives from pixels  
        reporting the state of the game that generates consequences in training  
        streams; here, proprioception (e.g., paddle location) rewards and  
        punishments. Fast structure learning is based on a long run of  
        pseudorandom play, picking out episodes that end in a reward, which are  
        appended or merged into the renormalising model (RGM). The second stage  
        of structure learning engages purposeful behaviour to learn the  
        transitions among rewarded episodes. Here, purposeful behaviour is  
        induced using expected cost at each level of the RGM and inductive  
        inference in the space of generalised states (i.e., episodes at the  
        highest level. Finally, the mapping from the leading stream (pixels) to  
        training streams is used to merge states at the highest level to compress  
        or reduce the model in a way that preserves the mutual information (i.e.,  
        expected free energy) between cause (i.e., first stream episodes) and  
        consequences (i.e., policies, rewards and cost).  
       __________________________________________________________________________  
        Copyright (C) 2019 Wellcome Trust Centre for Neuroimaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/DEM_AtariII.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("DEM_AtariIII", *args, **kwargs)
