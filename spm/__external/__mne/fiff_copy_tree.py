from spm._runtime import Runtime


def fiff_copy_tree(*args, **kwargs):
    """
       
           fiff_copy_tree(fidin, in_id, nodes, fidout)  
         
           Copies directory subtrees from fidin to fidout  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/fiff_copy_tree.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_copy_tree", *args, **kwargs, nargout=0)
