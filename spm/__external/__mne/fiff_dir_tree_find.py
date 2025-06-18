from mpython import Runtime


def fiff_dir_tree_find(*args, **kwargs):
    """

        [nodes] = fiff_dir_tree_find(tree,kind)

        Find nodes of the given kind from a directory tree structure


    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/fiff_dir_tree_find.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_dir_tree_find", *args, **kwargs)
