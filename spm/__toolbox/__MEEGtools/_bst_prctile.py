from spm.__wrapper__ import Runtime


def _bst_prctile(*args, **kwargs):
    """
      BST_PRCTILE: Returns the percentile value in vector  
         
        USAGE: value = bst_prctile(vector, percentile)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/MEEGtools/private/bst_prctile.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("bst_prctile", *args, **kwargs)
