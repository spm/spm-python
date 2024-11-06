from spm.__wrapper__ import Runtime


def _iscompatwrapper(*args, **kwargs):
    """
     ISCOMPATWRAPPER Checks whether the specified function name will invoke a  
        compatibility wrapper or not.  
         
        Copyright (C) 2012, Donders Centre for Cognitive Neuroimaging, Nijmegen, NL  
         
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
         
        $Id  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/iscompatwrapper.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("iscompatwrapper", *args, **kwargs)
