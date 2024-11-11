from spm.__wrapper__ import Runtime


def ft_anonymizedata(*args, **kwargs):
    """
      FT_ANONYMIZEDATA clears the value of potentially identifying fields in  
        the data and in the provenance information, i.e., it updates the data and  
        the configuration structure and history that is maintained by FieldTrip  
        in the cfg field.  
         
        Use as  
          output = ft_anonymizedata(cfg, data)  
        where data is any FieldTrip data structure and cfg is a configuration  
        structure that should contain  
          cfg.keepnumeric = 'yes' or 'no', keep numeric fields (default = 'yes')  
          cfg.keepfield   = cell-array with strings, fields to keep (default = {})  
          cfg.removefield = cell-array with strings, fields to remove (default = {})  
          cfg.keepvalue   = cell-array with strings, values to keep (default = {})  
          cfg.removevalue = cell-array with strings, values to remove (default = {})  
         
        The graphical user interface consists of a table that shows the name and  
        value of each provenance element, and whether it should be kept or  
        removed. Furthermore, it has a number of buttons:  
          - sort        specify which column is used for sorting  
          - apply       apply the current selection of 'keep' and 'remove' and hide the corresponding rows  
          - keep all    toggle all visibe rows to 'keep'  
          - remove all  toggle all visibe rows to 'keep'  
          - clear all   clear all visibe rows, i.e. neither 'keep' nor 'remove'  
          - quit        apply the current selection of 'keep' and 'remove' and exit  
         
        To facilitate data-handling and distributed computing you can use  
          cfg.inputfile  = ...  
          cfg.outputfile  = ...  
        If you specify one of these (or both) the input data will be read from a *.mat  
        file on disk and/or the output data will be written to a *.mat file. These mat  
        files should contain only a single variable, corresponding with the  
        input/output structure.  
         
        See also FT_DEFACEVOLUME, FT_DEFACEMESH, FT_ANALYSISPIPELINE  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_anonymizedata.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_anonymizedata", *args, **kwargs)
