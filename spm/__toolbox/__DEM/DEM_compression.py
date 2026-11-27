from spm._runtime import Runtime


def DEM_compression(*args, **kwargs):
    r"""
      Structure learning from pixels  
       __________________________________________________________________________  
         
        This routine demonstrates the mapping from pixels to (discrete)  
        representations of episodes. It illustrates the use of a certain kind of  
        deep generative model based upon reduction and grouping operators (RG)  
        found in the renormalisation group. In brief, this allows an efficient  
        encoding (and generation) of high dimensional content by maintaining  
        conditionally independent partitions of hidden states in a recursive  
        fashion. This example takes the view of efficient inference as,  
        effectively, compression and efficient coding of videos. However, the  
        focus of this compressed encoding is on the trajectory or path as visual  
        objects move.  
          
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
        lowest level and, effectively, encode a trajectory over to the 2^n  
        timesteps, where n is the depth of the model.  
         
       __________________________________________________________________________  
        Copyright (C) 2019 Wellcome Trust Centre for Neuroimaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/DEM_compression.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("DEM_compression", *args, **kwargs)
