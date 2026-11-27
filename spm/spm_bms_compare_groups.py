from spm._runtime import Runtime


def spm_bms_compare_groups(*args, **kwargs):
    r"""
      Compare BMS maps for different groups  
        FORMAT con_image = spm_bms_compare_groups(BMSfiles,name,contrast)  
         
        Input (interactive):  
        BMS             - BMS.mat files for the two groups to compare  
        contrast (name) - name of contrast image that will be save in the current  
                          directory   
        contrast (comp) - comparison between groups. options: 'A>B' (posterior   
                          probability for group 1 > posterior group 2)   
                          or 'A<B' (posterior probability group 1 <   
                          posterior for group 2)  
         
        Output: contrast image (path)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_bms_compare_groups.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_bms_compare_groups", *args, **kwargs)
