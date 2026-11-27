from spm._runtime import Runtime


def _combineClusters2(*args, **kwargs):
    r"""
      COMBINECLUSTERS2 is a helper function for FINDCLUSTER. It searches for  
        adjacent clusters in neighbouring channels and combines them. This  
        version is an alternative to the original m-file, and an alternative to  
        the mex-file. In some cases it may be faster, specifically if the spatial  
        adjacency matrix is large (size(C,1)>10000), and the number of columns in  
        the input data labelmat is low. Note also, that this version  
        supports a sparse adjacency matrix.  
         
        A mex-file is available for this functionality, as it can take quite long.  
        This mex-file is preferred if the spatial dimension is relatively small  
        (<1000).   
         
        Note that there is a minute difference in functional behaviour between  
        COMBINECLUSTERS and COMBINECLUSTERS2, where the former occasionally  
        labels isolated pixels (i.e. singleton 'clusters' in a spatial slice of  
        the labelmat) as a separate clusters, whereas COMBINECLUSTERS2 merges these  
        isolated pixels with the cluster in neighbouring slices (provided the  
        said isolated pixels is also suprathrehold in the neighbouring slice).  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/combineClusters2.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("combineClusters2", *args, **kwargs)
