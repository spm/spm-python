from spm._runtime import Runtime


def spm_get_anatomical_layout(*args, **kwargs):
    r"""
      Produce anatomically valid 2D representation of 3D sensor positions  
        FORMAT [lay] = spm_get_anatomical_layout(sensor_positions, sensor_labels, head_positions, fiducials, plot_output)  
         
        Input Parameters:  
            sensor_positions: An nx3 matrix representing the 3D Cartesian  
                              coordinates (x, y, z) of n sensors.  
            sensor_labels:    An nx1 cell array containing labels for each sensor.  
            head_positions:   An mx3 matrix representing the coordinates of  
                              positions on the head.  
            fiducials:        Struct containing coordinates of fiducials.  
                fiducials.NAS = [1 x 3]  
                fiducials.LPA = [1 x 3]  
                fiducials.RPA = [1 x 3]  
                fiducials.INI = [1 x 3] - Optional  
                              Note, if fiducials.INI is not specified it will be  
                              estimated.  
            plot_output:      (optional) A logical value indicating whether to generate a  
                              plot of measurements taken in 3D, as well as the  
                              output layout.  
            unit:             (optional) A string, e.g. 'mm', will be estimated otherwise.  
            sensor_orientations:  (optional) An nx3 matrix of orientation vectors of n  
                                  sensors  
         
        Output:  
            lay: A structure representing the anatomical sensor layout in the  
                FieldTrip style. It contains the following fields:  
                lay.pos:      A nx2 matrix representing the 2D coordinates of the  
                              sensors in the layout. Each column contains the  
                              [x, y] coordinates of a sensor relative to the  
                              vertex (Cz).  
                lay.label:    A cell array containing labels for each sensor.  
                lay.outline:  A cell array of matrices representing the 2D  
                              coordinates of the head surface outline, ears and  
                              nose.  
                lay.mask:     A cell array containing a matrix of positions which  
                              draw a convex hull around lay.pos to mask grid  
                              positions which would otherwise be extrapolated to  
                              when plotting.  
                              To allow extrapolation to a full circle, try:  
                              lay.mask{1} = lay.outline{1}.  
                lay.ori:      If sensor_orientations are provided then equivalent  
                              2D orientations are calculated.   
         
       __________________________________________________________________________  
         
        Further help:  
         
        spm_get_anatomical_layout is a function that defines the scalp surface  
        according to the approximate polar grid used to place electrodes in the  
        10-20 system. The method then measures the position of on-scalp sensors  
        in relation to this polar grid (angle and eccentricity) and applies this  
        to a standard 2D polar grid. For full details, or to cite this method see  
        Alexander et al (2025) available here: https://doi.org/10.1111/ejn.70060.  
         
        The function performs the following steps:  
         
          Get Anterior-Posterior and Left-Right Vectors:  
            Vectors defining the anterior-posterior and left-right directions on  
            the head surface are calculated. The vertex (Cz) position on the head  
            is then estimated, such that, for measurements taken across the scalp,  
            vertex->left, vertex->right are of equal length and vertex->anterior,  
            vertex-posterior are of equal lengths.  
         
          Create the approximate polar grid across the scalp.  
            Lines across the scalp are made based on the vectors described above.  
            These lines are then shortened according to the 10-20 method to  
            produce a grid with Fz, Oz, T3, T4 positions are the periphery. The  
            circumference around these points is then defined.  
         
          Define Sensor Position Relative to Cz:  
            Sensor positions are projected onto the scalp surface and their  
            position in relation to the vertex and circumference are defined.  
            Specifically, the distance from Cz to projected sensor position  
            relative to the distance from Cz to the circumference along the same  
            axis is taken. The relative distance from the point this axis crosses  
            the circumference to the nearest peripheral landmarks (e.g. Fz, T3)  
            determines the angle.  
         
          Define Sensor Position on a 2D Circle:  
            Using the eccentricity and angle measurements from the previous step,  
            the position of each sensor is reproduced on a 2D polar grid. This is  
            then formatted as a FieldTrip style layout structure with a nose,  
            ears, outline and mask.  
         
          (optional) Represent Sensor Orientations in 2D:  
            A tangential basis is defined in both 3D and 2D as an line (across the  
            scalp) from RPA to LPA, passing through the sensor position. The  
            local direction of the arc at the sensor position defined the primary  
            tangential axis. Radial is defined as a vector towards the origin.  
            Secondary primary axis as the cross product of primary and radial  
            axes. In 2D, magnitude is scaled by radial similarity.   
       _________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_get_anatomical_layout.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_get_anatomical_layout", *args, **kwargs)
