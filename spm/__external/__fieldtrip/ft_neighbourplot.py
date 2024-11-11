from spm.__wrapper__ import Runtime


def ft_neighbourplot(*args, **kwargs):
    """
      FT_NEIGHBOURPLOT visualizes neighbouring channels in a particular channel  
        configuration. The positions of the channel are specified in a  
        gradiometer or electrode configuration or from a layout.  
         
        Use as  
          ft_neighbourplot(cfg)  
        or as  
          ft_neighbourplot(cfg, data)  
         
        Where the configuration can contain  
          cfg.verbose       = string, 'yes' or 'no', whether the function will print feedback text in the command window  
          cfg.neighbours    = neighbourhood structure, see FT_PREPARE_NEIGHBOURS (optional)  
          cfg.enableedit    = string, 'yes' or 'no', allows you to interactively add or remove edges between vertices (default = 'no')  
          cfg.visible       = string, 'on' or 'off' whether figure will be visible (default = 'on')  
          cfg.figure        = 'yes' or 'no', whether to open a new figure. You can also specify a figure handle from FIGURE, GCF or SUBPLOT. (default = 'yes')  
          cfg.position      = location and size of the figure, specified as [left bottom width height] (default is automatic)  
          cfg.renderer      = string, 'opengl', 'zbuffer', 'painters', see MATLAB Figure Properties. If this function crashes, you should try 'painters'.  
         
        and either one of the following options  
          cfg.layout        = filename of the layout, see FT_PREPARE_LAYOUT  
          cfg.elec          = structure with electrode positions or filename, see FT_READ_SENS  
          cfg.grad          = structure with gradiometer definition or filename, see FT_READ_SENS  
          cfg.opto          = structure with gradiometer definition or filename, see FT_READ_SENS  
         
        If cfg.neighbours is not defined, this function will call  
        FT_PREPARE_NEIGHBOURS to determine the channel neighbours. The  
        following data fields may also be used by FT_PREPARE_NEIGHBOURS  
          data.elec         = structure with electrode positions  
          data.grad         = structure with gradiometer definition  
          data.opto         = structure with optode definition  
         
        If cfg.neighbours is empty, no neighbouring sensors are assumed.  
         
        Use cfg.enableedit to interactively add or remove edges in your own neighbour structure.  
         
        See also FT_PREPARE_NEIGHBOURS, FT_PREPARE_LAYOUT  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_neighbourplot.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_neighbourplot", *args, **kwargs)
