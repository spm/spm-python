from spm._runtime import Runtime


def fiff_list_dir_tree(*args, **kwargs):
    """
       
        fiff_list_dir_tree(fid, tree)  
         
        List the fiff directory tree structure  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/fiff_list_dir_tree.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_list_dir_tree", *args, **kwargs, nargout=0)
