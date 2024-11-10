from spm.__wrapper__ import Runtime


def _np_readfileinfo(*args, **kwargs):
    """
       
        function [np_info] = np_readfileinfo (filename, option)  
         
        Purpose:  
         
        np_readfileinfo reads out header information from a NEURO PRAX  
        data file (*.EEG).  
         
        Syntax:  
          
          [np_info] = np_readfileinfo(filename);  
          [np_info] = np_readfileinfo(filename,'NO_MINMAX');  
         
        Input data:  
         
          filename        -   the complete filename with path  
                              (e. g.  C:\Document...\20030716103637.EEG)  
          option          -   if option = 'NO_MINMAX' then physical minima  
          (optional)          and maxima off all channels will not be calculated  
                              (faster for long recordings)  
         
        Output data:  
         
          np_info         -   structure  
         
             np_info.filename       -   filename of *.EEG file  
             np_info.pathname       -   pathname of *.EEG file  
             np_info.name           -   patient's name  
             np_info.firstname      -   patient's firstname  
             np_info.birthday       -   patient's birthday  
             np_info.ID             -   identification number  
             np_info.date           -   start date of the recording (format: 'dd-mmm-yyyy')  
             np_info.time           -   start time of the recording (format: 'hh:mm:ss')  
             np_info.duration       -   duration of the recording (global for splitted EEG files!)  
             np_info.setup          -   electrode setup  
             np_info.pmtype         -   type of primary montage  
             np_info.algorithm      -   used algorithm for measurement  
             np_info.channels       -   cell-array with channel names  
             np_info.channeltypes   -   cell-array with channel types  
             np_info.units          -   cell-array with channel units  
             np_info.PhysMin        -   physical minimum for each channel (global for splitted EEG files!)  
             np_info.PhysMax        -   physical maximum for each channel (global for splitted EEG files!)  
             np_info.N              -   number of samples per channel (global for splitted EEG files!)  
             np_info.K              -   number of channels  
             np_info.fa             -   sampling frequency  
             np_info.fp_data        -   filepointer to data  
        --- additional SPLITTING information ---  
             np_info.SPLIT_Z        -   number of splitted EEG files (=Z; Z = 1 : no splitting)  
             np_info.SPLIT_filename -   all filenames of splitted EEG file (Zx1 cell-array)  
             np_info.SPLIT_N        -   samples of splitted EEG file (Zx1 array)  
             np_info.SPLIT_fp_data  -   file pointers of splitted EEG file (Zx1 array)  
             np_info.SPLIT_PhysMin  -   physical minimum for each channel and each file (ZxK array)  
             np_info.SPLIT_PhysMax  -   physical maximum for each channel and each file (ZxK array)  
         
        Version:  1.3. (2005-09-19)  
         
        (1) The field 'units' will be read correctly from the channel header.  
         
        (2) The sampling frequency (fa) is identical for all channels and is set  
            to the value of the first channel.  
         
        (3) The channel types will be read from the channel header directly.  
         
        (4) The field 'time' is set to the correct recording time.  
         
        (5) Additional structure fields:   
            setup      -   the electrode setup (previously "primmon")  
            pmtype     -   the type of the primary montage  
            algorithm  -   the feedback algorithm  
         
        (6) No longer available: the structure field "primmon".  
         
        (7) Splitted EEG files will be supported.  
         
        See also: np_readdata, np_readmarker  
         
        eldith GmbH  
        Gustav-Kirchhoff-Str. 5  
        D-98693 Ilmenau  
        Germany  
        02.02.2005  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/np_readfileinfo.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("np_readfileinfo", *args, **kwargs)
