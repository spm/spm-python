from spm.__wrapper__ import Runtime


def _np_readmarker(*args, **kwargs):
    """
       
        function [np_marker] = np_readmarker (filename, idx_begin, data_length, option)  
         
        np_readmarker reads marker from a NEURO PRAX marker file (*.EE_).  
         
        Syntax:  
         
          [np_marker] = np_readdata(filename,idx_begin,data_length,'samples');  
          [np_marker] = np_readdata(filename,idx_begin,data_length,'time');  
         
        Input data:  
         
          filename    -   the complete filename with path  
                          (e. g.  C:\Document...\20030716103637.EEG)  
          idx_begin   -   the start index of the data block to be read  
          data_length -   the length of the data block to be read  
          option      -   if option = 'samples':  
                              marker will be read from sample index 'idx_begin'  
                              to sample index 'idx_begin' + 'data_length' - 1  
                          if option = 'time':  
                              marker will be read from time index 'idx_begin'  
                              to time index 'idx_begin' + 'data_length'  
         
                          To read all markers use: idx_start = 0, data_length = inf, option =  
                          'samples'.  
         
        Output data:  
         
          np_marker        -   structure  
         
             np_marker.markernames   -   cell-array with markernames   
             np_marker.markertyp     -   vector array with markertypes  
             np_marker.marker        -   cell-array with marker vectors   
                                         ( = sample indices if option = 'samples',  
                                           = time indices if option = 'time');  
         
        Version:  1.2. (2005-01-19)  
                  1.1. (2004-10-22)  
         
        1. Artefact trials will not be considered.  
        2. Trials within pause intervals will not be considered.  
         
        See also: np_readfileinfo, np_readdata  
         
        eldith GmbH  
        Gustav-Kirchhoff-Str. 5  
        D-98693 Ilmenau  
        Germany  
        22.10.2004  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/np_readmarker.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("np_readmarker", *args, **kwargs)
