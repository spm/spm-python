from spm._runtime import Runtime


def mne_read_label_file(*args, **kwargs):
    r"""
       
        [label] = mne_read_label_file(filename)  
          
        Reads a label file. The returned structure has the following fields  
         
            comment        comment from the first line of the label file  
            vertices       vertex indices (0 based, column 1)  
            pos            locations in meters (columns 2 - 4 divided by 1000)  
            values         values at the vertices (column 5)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/mne_read_label_file.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mne_read_label_file", *args, **kwargs)
