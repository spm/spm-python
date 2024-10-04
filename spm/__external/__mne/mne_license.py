from spm.__wrap__ import _Runtime


def mne_license(*args, **kwargs):
  """  MNE_LICENSE prints the license only once upon the first call to  
    this function. If the user does a "clear all", the license will  
    again be shown.  This function should be included in every openmeeg  
    function to ensure that the license is displayed at least once.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/mne_license.m)
  """

  return _Runtime.call("mne_license", *args, **kwargs, nargout=0)
