from spm.__wrapper__ import Runtime


def fiff_invert_transform(*args, **kwargs):
    """
       
        [itrans] = fiff_invert_transform(trans)  
         
        Invert a coordinate transformation  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/fiff_invert_transform.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("fiff_invert_transform", *args, **kwargs)
