from spm.__wrapper__ import Runtime


def _np_readdata(*args, **kwargs):
    """
       
        function [np_data] = np_readdata (filename, idx_begin, data_length, option)  
         
        np_readdata reads data from a NEURO PRAX data file (*.EEG).  
         
         
        Syntax:  
         
          [np_data] = np_readdata(filename,idx_begin,data_length,'samples');  
          [np_data] = np_readdata(filename,idx_begin,data_length,'time');  
         
        Input data:  
         
          filename    -   the complete filename with path  
                          (e. g.  C:\Document...\20030716103637.EEG)  
          idx_begin   -   the start index of the data block to be read  
          data_length -   the length of the data block to be read  
          option      -   if option = 'samples':  
                              the data block starts at sample 'idx_begin' from the recording;  
                              data_length is the number of samples to be read  
                          if option = 'time':  
                              the data block starts at time 'idx_begin' from the recording;  
                              data_length is the number of seconds to be read  
         
                          To read all data use: idx_start = 0, data_length = inf, option =  
                          'samples'.  
         
        Output data:  
         
          np_data     -   structure  
             np_data.data     -   data matrix of unipolar raw data  
                                  dimension of the matrix: (NxK)  
                                  N: number of samples  
                                  K: number of channels (each column is one channel)  
             np_data.t        -   discrete time vector for the recording  
         
        Version:  1.2. (2005-02-02)  
         
        See also: np_readfileinfo, np_readmarker  
         
        eldith GmbH  
        Gustav-Kirchhoff-Str. 5  
        D-98693 Ilmenau  
        Germany  
        02.02.2005  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/np_readdata.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("np_readdata", *args, **kwargs)
