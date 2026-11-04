from spm._runtime import Runtime


def fiff_dir_tree_find(*args, **kwargs):
    r"""
       
        [nodes] = fiff_dir_tree_find(tree,kind)  
         
        Find nodes of the given kind from a directory tree structure  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/fiff_dir_tree_find.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_dir_tree_find", *args, **kwargs)
