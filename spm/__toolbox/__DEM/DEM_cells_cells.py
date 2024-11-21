from spm.__wrapper__ import Runtime


def DEM_cells_cells(*args, **kwargs):
    """
      This demo is a hierarchical extension of DEM_cells.m, where we have 16  
        ensembles comprising 16 cells. Each cell has a generative model (i.e.,  
        prior beliefs) about its possible local and global cell types (i.e.,  
        internal, active or sensory). Given posterior beliefs about what sort of  
        self it is at the local and global level, it can then predict the local  
        and global intracellular signals it would expect to receive. The ensemble  
        of ensembles then converges to a point attractor; where the ensemble has  
        a Markov blanket and each element of the ensemble comprises a cell - that  
        is itself a Markov blanket. The focus of this simulation is how the local  
        level couples to the global level and vice versa. For simplicity (and  
        computational expediency) we only model one ensemble at the local level  
        and assume that the remaining ensembles conform to the same (local)  
        dynamics. This is effectively a mean field approximation, where  
        expectations of a cell in the first ensemble about its global type are  
        coupled to the corresponding expectations and the ensemble level, and  
        vice versa. The results of this simulation are provided in the form of a  
        movie and graphs.The figure legend is included in the code below.  
         
        In this example, we have used the same generative model at both levels to  
        exploit the self similar hierarchical structure that emerges. However, we  
        could have used different generative models at the global and local  
        levels to simulate the morphogenesis of particular organelles that have a  
        different form from their constituent cellular ensembles.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_cells_cells.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_cells_cells", *args, **kwargs)
