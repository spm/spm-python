from spm._runtime import Runtime


def DEM_Tower(*args, **kwargs):
    r"""
      Demo of planning as sophisticated inference (Tower of Hanoi)  
       __________________________________________________________________________  
         
        This demonstration routine illustrates planning as inductive  
        inference in the context of the Tower of Hanoi paradigm.  
        This is effectively a game in which coloured blocks have to be moved  
        between (usually three) pillars or towers to achieve a target  
        arrangement. The generative model in this instance is based upon the  
        notion of latent states as arrangements of multiple objects; where the  
        physics — underwriting the generative model — prescribes allowable  
        transitions among arrangements. In this example, a generative process is  
        set up by associating every possible arrangement of blocks in three  
        towers with latent states. These latent states generate outcomes for each  
        location (i.e., a coloured block or nothing for each visual modality).  
        Transitions among arrangements are modelled as  controllable paths,  
        corresponding to choosing a particular pillar and moving the top block to  
        another pillar (or doing nothing).  
       _________________________________________________________________________  
        Copyright (C) 2019 Wellcome Trust Centre for Neuroimaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/DEM_Tower.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("DEM_Tower", *args, **kwargs)
