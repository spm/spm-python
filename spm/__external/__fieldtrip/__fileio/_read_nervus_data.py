from spm.__wrapper__ import Runtime


def _read_nervus_data(*args, **kwargs):
    """
      read_nervus_data  Returns data from Nicolet file.  
         
          OUT = read_nervus_data(NRVHDR, SEGMENT, RANGE, CHIDX) returns data in an n x m array of  
          doubles where n is the number of datapoints and m is the number  
          of channels.  
         
          NRVHDR is a header from the function read_nervus_header  
          SEGMENT is the segment number in the file to read from  
          RANGE is a 1x2 array with the [StartIndex EndIndex]  - default: all  
          and CHIDX is a vector of channel indeces - default: all  
         
          FILENAME is the file name of a file in the Natus/Nicolet/Nervus(TM)  
          format (originally designed by Taugagreining HF in Iceland)  
         
          Based on ieeg-portal/Nicolet-Reader  
          at https://github.com/ieeg-portal/Nicolet-Reader  
         
        Copyright (C) 2016, Jan Brogger and Joost Wagenaar   
         
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
         
        $Id: $  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_nervus_data.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_nervus_data", *args, **kwargs)
