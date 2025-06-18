from mpython import Runtime


def _bst_progress(*args, **kwargs):
    """
      Dummy function to be able to use BST code unmodified


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/MEEGtools/private/bst_progress.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("bst_progress", *args, **kwargs)
