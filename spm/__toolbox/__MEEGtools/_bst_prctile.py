from spm._runtime import Runtime


def _bst_prctile(*args, **kwargs):
    r"""
      BST_PRCTILE: Returns the percentile value in vector  
         
        USAGE: value = bst_prctile(vector, percentile)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/MEEGtools/private/bst_prctile.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("bst_prctile", *args, **kwargs)
