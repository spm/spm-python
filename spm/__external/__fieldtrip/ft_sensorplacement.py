from spm._runtime import Runtime


def ft_sensorplacement(*args, **kwargs):
    r"""
      FT_SENSORPLACEMENT positions sensor sensor holders over the surface of the scalp (when  
        wearing a flexible cap) or over the surface of a rigid 3D-printed helmet. It uses  
        a model of the sensor sensor and sensor holder, copies this repeatedly, and positions  
        and orients it for each desired sensor position. The sensor positions are automatically  
        determined based on a template distribution, for example the 10-20 electrode placement  
        scheme or a equidistant placement scheme, but you can also provide your own sensor  
        positions.  
         
        Use as  
          [cfg, sensors] = ft_sensorplacement(cfg, headshape)  
        where the headshape represents the scalp surface from FT_PREPARE_MESH or  
        FT_MESHREALIGN. This function returns a structure array with a number of  
        meshes representing the sensor sensors or sensor holders that can be plotted.  
         
        The input configuration structure can contain the following  
          cfg.template      = string, filename with the STL model of the sensor or sensor holder  
          cfg.write         = 'no' or 'yes', write the sensors to STL files  
          cfg.elec          = structure with electrode positions or filename, see FT_READ_SENS  
          cfg.channel       = cell-array, selection of electrode locations at which to place an sensor sensor  
          cfg.outwardshift  = number, amount to shift the sensors outward from the surface  
          cfg.rotx          = Nx1 vector with the rotation around the x-axis (default is automatic)  
          cfg.roty          = Nx1 vector with the rotation around the y-axis (default is automatic)  
          cfg.rotz          = Nx1 vector with the rotation around the z-axis (default is automatic)  
          cfg.grad          = structure with a single OPM sensor, see FT_DATATYPE_SENS  
         
        The output configuration structure contains the rotations that were performed,  
        which can be adjusted and used in a second iteration. The output sensor structure  
        array contains the geometrical description of all sensors, following rotation and  
        translation.  
         
        See also FT_ELECTRODEPLACEMENT, FT_PREPARE_MESH, FT_MESHREALIGN, FT_DEFACEMESH  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/ft_sensorplacement.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_sensorplacement", *args, **kwargs)
