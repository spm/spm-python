from spm.__wrapper__ import Runtime


def ft_select_voxel(*args, **kwargs):
    """
      FT_SELECT_VOXEL is a helper function that can be used as callback function  
        in a figure. It allows the user to select a voxel from a (resliced) 3-D volume.  
         
        Use as  
          voxel = ft_select_voxel(h, eventdata, ...)  
        The first two arguments are automatically passed by MATLAB to any  
        callback function.  
         
        Additional options should be specified in key-value pairs and can be  
          'callback'  = function handle to be executed after channels have been selected  
         
        You can pass additional arguments to the callback function in a cell-array  
        like {@function_handle,arg1,arg2}  
         
        Example  
          % create a figure with a random 3-D volume  
          mri = rand(128,128,128);  
          ft_plot_slice(mri, 'location', [64 64 64], 'orientation', [1 1 1]);  
          view(120,30)  
          xlabel('x'); ylabel('y'); zlabel('z'); grid on  
          axis([0 128 0 128 0 128])  
          axis equal; axis vis3d  
          axis([0 128 0 128 0 128])  
         
          % add this function as the callback to make a single selection  
          set(gcf, 'WindowButtonDownFcn', {@ft_select_voxel, 'callback', @disp})  
         
        Subsequently you can click in the figure and you'll see that the disp  
        function is executed as callback and that it displays the selected  
        voxel.  
         
        See also FT_SELECT_BOX, FT_SELECT_CHANNEL, FT_SELECT_POINT, FT_SELECT_POINT3D, FT_SELECT_RANGE  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/plotting/ft_select_voxel.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_select_voxel", *args, **kwargs, nargout=0)
