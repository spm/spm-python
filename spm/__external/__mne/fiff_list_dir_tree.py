from spm._runtime import Runtime


def fiff_list_dir_tree(*args, **kwargs):
    r"""
       
        fiff_list_dir_tree(fid, tree)  
         
        List the fiff directory tree structure  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/fiff_list_dir_tree.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_list_dir_tree", *args, **kwargs, nargout=0)
