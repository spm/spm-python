from spm._runtime import Runtime


def _select_channel_list(*args, **kwargs):
    r"""
      SELECT_CHANNEL_LIST presents a dialog for selecting multiple elements  
        from a cell-array with strings, such as the labels of EEG channels.  
        The dialog presents two columns with an add and remove mechanism.  
         
        select = select_channel_list(label, initial, titlestr)  
         
        with  
          initial indices of channels that are initially selected  
          label   cell-array with channel labels (strings)  
          titlestr    title for dialog (optional)  
        and  
          select  indices of selected channels  
         
        If the user presses cancel, the initial selection will be returned.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/select_channel_list.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("select_channel_list", *args, **kwargs)
