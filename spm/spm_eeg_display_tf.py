from spm.__wrapper__ import Runtime


def spm_eeg_display_tf(*args, **kwargs):
    """
      Display TF images saved as NIfTI  
        FORMAT spm_eeg_display_tf(files)  
        files  -  list of images to display (as char or cell array of strings)  
                  Up to 6 images are supported   
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_display_tf.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_display_tf", *args, **kwargs, nargout=0)
