from spm.__wrapper__ import Runtime


def dccnpath(*args, **kwargs):
    """
      DCCNPATH manages the filename and path for test files. It helps to locate and read  
        test file from Linux, Windows or macOS computers both inside and outside the DCCN.  
         
        Use as  
          filename = dccnpath(filename)  
        where the input filename corresponds to the test data on the DCCN cluster and the  
        output filename corresponds to the local file including the full path where the  
        test data is available.  
         
        The test data location on the DCCN cluster is '/home/common/matlab/fieldtrip/data'  
        and the specification of the input filename MUST start with this.  
         
        This function will search-and-replace the location on the DCCN cluster by the  
        location that applies to your computer. If needed, it will replace '/home' by 'H:'  
        and will replace forward by backward slashes.  
         
        In case you have a local copy of the data, or if you are inside the DCCN and have  
        mounted the '/home' drive on another letter than 'H:', you should override the  
        default location using  
           global ft_default  
           ft_default.dccnpath = '/your/copy';  
         
        If you DO HAVE a local copy, it should contain a directory with the name 'ftp'. The   
        content of the ftp directory should match that on the FieldTrip download server,   
        for example '/your/copy/ftp/test/ctf'.  
         
        If you DO NOT have a local copy and do not define ft_default.dccnpath manually,  
        then this function will automatically try to download the publicly available data   
        to a temporary directory.  
         
        See also WHICH, WEBSAVE  
        Copyright (C) 2012-2024, Donders Centre for Cognitive Neuroimaging, Nijmegen, NL  
         
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/dccnpath.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("dccnpath", *args, **kwargs)
