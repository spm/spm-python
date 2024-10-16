from spm.__wrapper__ import Runtime


def spm_Menu(*args, **kwargs):
  """  SPM Menu window  
    FORMAT Fmenu = spm_Menu('Create',Vis)  
    Create the SPM Menu window (tag property set to 'Menu')  
    Vis    - visibility: {'on'} or 'off'  
    Fmenu  - handle of figure created  
     
    FORMAT Fmenu = spm_Menu('Switch',Modality)  
    Switch the SPM Menu window to the specified modality  
     
    FORMAT spm_Menu('Close')  
    Close the SPM Menu window  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_Menu.m)
  """

  return Runtime.call("spm_Menu", *args, **kwargs)
