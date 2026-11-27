from spm._runtime import Runtime


def _read_labview_dtlg(*args, **kwargs):
    r"""
      READ_LABVIEW_DTLG  
         
        Use as  
          dat = read_labview_dtlg(filename, datatype)  
        where datatype can be 'int32' or 'int16'  
         
        The output of this function is a structure.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/read_labview_dtlg.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_labview_dtlg", *args, **kwargs)
