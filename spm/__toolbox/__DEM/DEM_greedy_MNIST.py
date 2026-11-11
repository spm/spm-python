from spm._runtime import Runtime


def DEM_greedy_MNIST(*args, **kwargs):
    r"""
      Structure learning from pixels  
       __________________________________________________________________________  
         
        This routine demonstrates the mapping from pixels to (discrete)  
        representations of episodes. It illustrates the use of a certain kind of  
        deep generative model based upon reduction and grouping operators (RG)  
        found in the renormalisation group. In brief, this allows an efficient  
        encoding (and generation) of high dimensional content by maintaining  
        conditionally independent partitions of hidden states in a recursive  
        fashion.  
         
        This example uses image classification to showcase the ability of  
        recursive generative models to compress images in a way that leverages  
        the composition of small image components into larger arrangements. Uses  
        the MNIST digit classification problem. In brief, images are discretised  
        using singular value decomposition of local image patches. These are then  
        recursively assembled using a fast structure learning routine. Subsequent  
        training images and then assimilated using parametric learning. The  
        ensuing generative model is then illustrated in terms of digit  
        classification and the underlying architecture.  
         
       __________________________________________________________________________  
        Copyright (C) 2019 Wellcome Trust Centre for Neuroimaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/DEM_greedy_MNIST.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("DEM_greedy_MNIST", *args, **kwargs)
