from spm._runtime import Runtime


def mne_label_time_courses(*args, **kwargs):
    """
       
        function [ values, times ] = mne_label_time_courses(labelfile,stcfile)  
         
        Extract the time courses corresponding to a label file from an stc file  
         
        labelfile - The name of the label file  
        stcfile   - The name of the stc file (must be on the same subject and  
        hemisphere as the stc file  
         
        values    - The time courses  
        times     - The time points  
        vertices  - The vertices corresponding to the time points  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/mne_label_time_courses.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mne_label_time_courses", *args, **kwargs)
