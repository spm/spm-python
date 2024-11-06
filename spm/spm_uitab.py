from spm.__wrapper__ import Runtime


def spm_uitab(*args, **kwargs):
    """
      Create tabs in a figure  
        FORMAT [handles] = spm_uitab(hparent,labels,callbacks,tag,active,height,tab_height)  
        This function creates tabs in the SPM graphics window.  
        These tabs may be associated with different sets of axes and uicontrol,  
        through the use of callback functions linked to the tabs.  
        Inputs:  
          hparent    - the handle of the parent of the tabs (can be the SPM  
                       graphics windows, or the handle of the uipanel of a former  
                       spm_uitab...)  
          labels     - a cell array of string containing the labels of the tabs  
          callbacks  - a cell array of strings which will be evaluated using the  
                       'eval' function when clicking on a tab [default: {[]}]  
          tag        - a string which is the tag associated with the tabs  
                       (useful for finding them in a window...) [default: '']  
          active     - the index of the active tab when creating the uitabs  
                       [default: 1, ie the first tab is active]  
          height     - the relative height of the tab panels within its parent  
                       spatial extent [default: 1]  
          tab_height - the relative height of the tabs within its parent spatial  
                       extent [default: 0.025]  
        Output:  
          handles    - a structure of handles for the different tab objects.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_uitab.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_uitab", *args, **kwargs)
