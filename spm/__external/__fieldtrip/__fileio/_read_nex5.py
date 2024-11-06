from spm.__wrapper__ import Runtime


def _read_nex5(*args, **kwargs):
    """
      READ_NEX5 reads header or data from a Nex Technologies *.nex5 file,   
        which is a file containing action-potential (spike) timestamps and waveforms  
        (spike channels), event timestamps (event channels), and continuous  
        variable data (continuous A/D channels).  
         
        LFP and spike waveform data that is returned by this function is   
        expressed in microVolt.  
         
        Use as  
          [hdr] = read_nex5(filename)  
          [dat] = read_nex5(filename, ...)  
          [dat1, dat2, dat3, hdr] = read_nex5(filename, ...)  
         
        Optional arguments should be specified in key-value pairs and can be  
          header      structure with header information  
          feedback    0 or 1  
          tsonly      0 or 1, read only the timestamps and not the waveforms  
          channel     number, or list of numbers (that will result in multiple outputs)  
          begsample   number (for continuous only)  
          endsample   number (for continuous only)  
         
        See also READ_NEX5_HEADER  
         
        Copyright (C) 2020 Robert Oostenveld, Alex Kirillov  
         
        This file is part of FieldTrip, see http://www.fieldtriptoolbox.org  
        for the documentation and details.  
         
           FieldTrip is free software: you can redistribute it and/or modify  
           it under the terms of the GNU General Public License as published by  
           the Free Software Foundation, either version 3 of the License, or  
           (at your option) any later version.  
         
           FieldTrip is distributed in the hope that it will be useful,  
           but WITHOUT ANY WARRANTY; without even the implied warranty of  
           MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the  
           GNU General Public License for more details.  
         
           You should have received a copy of the GNU General Public License  
           along with FieldTrip. If not, see <http://www.gnu.org/licenses/>.  
         
        $Id$  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_nex5.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_nex5", *args, **kwargs)
