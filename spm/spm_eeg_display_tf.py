from spm._runtime import Runtime


def spm_eeg_display_tf(*args, **kwargs):
    r"""
      Display TF images saved as NIfTI  
        FORMAT spm_eeg_display_tf(files)  
        files  -  list of images to display (as char or cell array of strings)  
                  Up to 6 images are supported   
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_eeg_display_tf.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_display_tf", *args, **kwargs, nargout=0)
