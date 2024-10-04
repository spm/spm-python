from spm.__wrap__ import _Runtime


def ft_save_workspace(*args, **kwargs):
  """  FT_SAVE_WORKSPACE saves every variable in the base workspace to a .mat file with  
    the same name as the variable in the workspace itself. For example, the variable  
    "ans" would be saved to the file "ans.mat". Prior to calling this function, you  
    might want to clean up your workspace using CLEAR or KEEP.  
     
    Use as  
      ft_save_workspace(dirname)  
     
    If the directory does not yet exist, this function will create it for you. If you  
    leave it empty, the files will be saved to the present working directory.  
     
    For example, the following will save all variables to a time-stamped  
    sub-directory that is created inside the present working directory:  
     
      ft_save_workspace(datestr(now))  
     
    See also SAVE, LOAD, SAVEFIG, CLEAR, KEEP  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/ft_save_workspace.m)
  """

  return _Runtime.call("ft_save_workspace", *args, **kwargs, nargout=0)
