from spm.__wrap__ import _Runtime


def spm_eeg_display_tf(*args, **kwargs):
  """  Display TF images saved as NIfTI  
    FORMAT spm_eeg_display_tf(files)  
    files  -  list of images to display (as char or cell array of strings)  
              Up to 6 images are supported   
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_eeg_display_tf.m)
  """

  return _Runtime.call("spm_eeg_display_tf", *args, **kwargs, nargout=0)
