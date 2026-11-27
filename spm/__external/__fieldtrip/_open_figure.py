from spm._runtime import Runtime


def _open_figure(*args, **kwargs):
    r"""
      OPEN_FIGURE is a helper function to open a figure with some specific settings  
        consistent over all FieldTrip functions that do plotting and/or that show a  
        graphical user interface.  
         
        See also GCA, GCF, GROOT,  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/open_figure.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("open_figure", *args, **kwargs)
