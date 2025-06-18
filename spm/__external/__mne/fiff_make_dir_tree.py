from mpython import Runtime


def fiff_make_dir_tree(*args, **kwargs):
    """

        [tree, last] = fiff_make_dir_tree(fid,dir,start,indent)

        Create the directory tree structure


    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/fiff_make_dir_tree.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_make_dir_tree", *args, **kwargs)
