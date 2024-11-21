from spm.__wrapper__ import Runtime


def spm_vb_graphcut(*args, **kwargs):
    """
      Recursive bi-partition of a graph using the isoperimetric algorithm  
          
        FORMAT labels = spm_vb_graphcut(labels,index,I,W,depth,grnd_type,CUTOFF,DIM)  
         
        labels     each voxel is lableled depending on which segment is belongs  
        index      index of current node set in labels vector  
        I          InMask XYZ voxel (node set) indices  
        W          weight matrix i.e. adjacency matrix containing edge weights   
                   of graph  
        depth      depth of recursion  
        grnd_type  'random' or 'max' - ground node selected at random or the   
                   node with maximal degree  
        CUTOFF     minimal number of voxels in a segment of the partition  
        DIM        dimensions of data  
       __________________________________________________________________________  
          
        Recursive bi-partition of a graph using the isoperimetric algorithm by   
        Grady et al. This routine is adapted from "The Graph Analysis Toolbox:   
        Image Processing on Arbitrary Graphs", available through Matlab Central  
        File Exchange. See also Grady, L. Schwartz, E. L. (2006) "Isoperimetric   
        graph partitioning for image segmentation",  
        IEEE Trans Pattern Anal Mach Intell, 28(3),pp469-75  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_vb_graphcut.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_vb_graphcut", *args, **kwargs)
