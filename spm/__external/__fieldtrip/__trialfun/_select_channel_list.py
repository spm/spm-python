from spm.__wrapper__ import Runtime


def _select_channel_list(*args, **kwargs):
    """
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/trialfun/private/select_channel_list.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("select_channel_list", *args, **kwargs)
