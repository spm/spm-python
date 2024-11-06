from spm.__wrapper__ import Runtime


def ft_plot_sens(*args, **kwargs):
    """
      FT_PLOT_SENS visualizes the EEG, MEG or NIRS sensor array.  
         
        Use as  
          ft_plot_sens(sens, ...)  
        where the first argument is the sensor array as returned by FT_READ_SENS or  
        by FT_PREPARE_VOL_SENS.  
         
        Optional input arguments should come in key-value pairs and can include  
          'label'           = show the label, can be 'off', 'label', 'number' (default = 'off')  
          'chantype'        = string or cell-array with strings, for example 'meg' (default = 'all')  
          'unit'            = string, convert the sensor array to the specified geometrical units (default = [])  
          'axes'            = boolean, whether to plot the axes of the 3D coordinate system (default = false)  
          'fontcolor'       = string, color specification (default = 'k')  
          'fontsize'        = number, sets the size of the text (default = 10)  
          'fontunits'       =  
          'fontname'        =  
          'fontweight'      =  
         
        The following options apply to MEG magnetometers and/or gradiometers  
          'coil'            = true/false, plot each individual coil (default = false)  
          'orientation'     = true/false, plot a line for the orientation of each coil (default = false)  
          'coilshape'       = 'point', 'circle', 'square', 'sphere', or 'disc' (default is automatic)  
          'coilsize'        = diameter or edge length of the coils (default is automatic)  
        The following options apply to EEG electrodes  
          'elec'            = true/false, plot each individual electrode (default = false)  
          'orientation'     = true/false, plot a line for the orientation of each electrode (default = false)  
          'elecshape'       = 'point', 'circle', 'square', 'sphere', or 'disc' (default is automatic)  
          'elecsize'        = diameter of the electrodes (default is automatic)  
          'headshape'       = headshape, required for elecshape 'disc'  
        The following options apply to NIRS optodes  
          'opto'            = true/false, plot each individual optode (default = false)  
          'orientation'     = true/false, plot a line for the orientation of each optode (default = false)  
          'optoshape'       = 'point', 'circle', 'square', 'sphere', or 'disc' (default is automatic)  
          'optosize'        = diameter of the optodes (default is automatic)  
          'headshape'       = headshape, required for optoshape 'disc'  
         
        The following options apply when electrodes/coils/optodes are NOT plotted individually  
          'style'           = plotting style for the points representing the channels, see plot3 (default = [])  
          'marker'          = marker type representing the channels, see plot3 (default = '.')  
        The following options apply when electrodes/coils/optodes are plotted individually  
          'facecolor'       = [r g b] values or string, for example 'brain', 'cortex', 'skin', 'black', 'red', 'r', or an Nx3 or Nx1 array where N is the number of faces (default is automatic)  
          'edgecolor'       = [r g b] values or string, for example 'brain', 'cortex', 'skin', 'black', 'red', 'r', color of channels or coils (default is automatic)  
          'facealpha'       = transparency, between 0 and 1 (default = 1)  
          'edgealpha'       = transparency, between 0 and 1 (default = 1)  
         
        The sensor array can include an optional fid field with fiducials, which will also be plotted.  
          'fiducial'        = rue/false, plot the fiducials (default = true)  
          'fidcolor'        = [r g b] values or string, for example 'red', 'r', or an Nx3 or Nx1 array where N is the number of fiducials  
          'fidmarker'       = ['.', '*', '+',  ...]  
          'fidlabel'        = ['yes', 'no', 1, 0, 'true', 'false']  
         
        Example:  
          sens = ft_read_sens('Subject01.ds', 'senstype', 'meg');  
          figure; ft_plot_sens(sens, 'coilshape', 'point', 'style', 'r*')  
          figure; ft_plot_sens(sens, 'coilshape', 'circle')  
          figure; ft_plot_sens(sens, 'coilshape', 'circle', 'coil', true, 'chantype', 'meggrad')  
          figure; ft_plot_sens(sens, 'coilshape', 'circle', 'coil', false, 'orientation', true)  
         
        See also FT_DATATYPE_SENS, FT_READ_SENS, FT_PLOT_HEADSHAPE, FT_PLOT_HEADMODEL,  
        FT_PLOT_TOPO3D  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/plotting/ft_plot_sens.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_plot_sens", *args, **kwargs)
