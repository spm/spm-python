from spm.__wrapper__ import Runtime


def _labelcmb2indx(*args, **kwargs):
    """
      LABELCMB2INDX computes an array with indices, corresponding to the order  
        in a list of labels, for an Nx2 list of label combinations  
         
        Use as  
          [indx] = labelcmb2indx(labelcmb, label)  
        or  
          [indx] = labelcmb2indx(labelcmb)  
         
        Labelcmb is an Nx2 cell-array with label combinations, label is an Mx1   
        cell-array with labels. If only one input is provided, the indices are  
        with respect to the rows in the labelcmb matrix, where the corresponding  
        auto combinations are located. As a consequence, the labelcmb matrix   
        needs to contain rows containing auto-combinations  
          
        Example:   
         labelcmb = {'a' 'b';'a' 'c';'b' 'c';'a' 'a';'b' 'b';'c' 'c'};  
         label    = {'a';'b';'c'};  
         
        indx = labelcmb2indx(labelcmb, label)  
         returns:  [1 2;1 3;2 3;1 1;2 2;3 3]  
          
        indx = labelcmb2indx(labelcmb)  
         returns:  [4 5;4 6;5 6;4 4;5 5;6;6]  
         
        This is a helper function to FT_CONNECTIVITYANALYSIS  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/labelcmb2indx.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("labelcmb2indx", *args, **kwargs)
