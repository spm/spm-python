from spm.__wrapper__ import Runtime


def _handle_edit_input(*args, **kwargs):
    """
      HANDLE_EDIT_INPUT deals with user-entered input in the GUI. This is used to select  
        channels and/or trials in FT_REJECTVISUAL and to select channels in FT_DATABROWSER  
         
        The input text can consist of a string such as  
          1 2 3 4  
          1:4  
          [1 2 3 4]  
          [1:4]  
        This is converted in a list of numbers.  
         
        The input text can also consist of a single non-numeric string or a string that  
        represents a cell-array of strings such as  
          all  
          {'MEG', '-MR*'}  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/handle_edit_input.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("handle_edit_input", *args, **kwargs)
