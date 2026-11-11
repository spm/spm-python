from spm._runtime import Runtime


def _bst_progress(*args, **kwargs):
    r"""
      Dummy function to be able to use BST code unmodified  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/MEEGtools/private/bst_progress.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("bst_progress", *args, **kwargs)
