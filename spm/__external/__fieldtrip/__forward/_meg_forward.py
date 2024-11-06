from spm.__wrapper__ import Runtime


def _meg_forward(*args, **kwargs):
    """
      calculates the magnetic field of n dipoles  
        in a realistic volume conductor  
        usage: field=meg_forward(dip_par,forwpar)  
         
        input:  
        dip_par nx6 matrix where each row contains location (first 3 numbers)  
                and moment (second 3 numbers) of a dipole  
        forwpar structure containing all information relevant for this  
                calculation; forwpar is calculated with meg_ini  
                You have here an option to include linear transformations in  
                the forward model by specifying forpwar.lintrafo=A  
                where A is an NxM matrix. Then field -> A field  
                You can use that, e.g., if you can write the forward model  
                with M magnetometer-channels plus a matrix multiplication  
                transforming this to a (eventually higher order) gradiometer.  
         
        output:  
        field  mxn matrix where the i.th column is the field in m channels  
               of the i.th dipole  
         
        note:  No assumptions about units are made (i.e. no scaling factors)  
         
        Copyright (C) 2003, Guido Nolte  
         
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/forward/private/meg_forward.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("meg_forward", *args, **kwargs)
