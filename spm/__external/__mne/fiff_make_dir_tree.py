from spm._runtime import Runtime


def fiff_make_dir_tree(*args, **kwargs):
    r"""
       
        [tree, last] = fiff_make_dir_tree(fid,dir,start,indent)  
         
        Create the directory tree structure  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/fiff_make_dir_tree.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_make_dir_tree", *args, **kwargs)
