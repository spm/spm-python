from spm.__wrapper__ import Runtime


def spm_slice_timing(*args, **kwargs):
    """
      Correct differences in slice acquisition times  
        FORMAT spm_slice_timing(P, sliceorder, refslice, timing, prefix)  
        P           - char array of image filenames  
                      can also be a cell array of the above (multiple subjects).  
        sliceorder  - slice acquisition order, a vector of integers, each  
                      integer referring the slice number in the image file  
                      (1=first), and the order of integers representing their  
                      temporal acquisition order  
                      OR vector containing the acquisition time for each slice  
                      in milliseconds  
        refslice    - slice for time 0  
                      OR time in milliseconds for the reference slice  
        timing      - additional information for sequence timing  
                      timing(1) = time between slices  
                                = TA / (nslices - 1)  
                      timing(2) = time between last slices and next volume  
                                = TR - TA  
                      OR timing = [0 TR] when previous inputs are specified in  
                      milliseconds  
        prefix      - filename prefix for corrected image files, defaults to 'a'  
       __________________________________________________________________________  
         
          Note: The sliceorder arg that specifies slice acquisition order is  
          a vector of N numbers, where N is the number of slices per volume.  
          Each number refers to the position of a slice within the image file.  
          The order of numbers within the vector is the temporal order in which  
          those slices were acquired.  
         
          To check the order of slices within an image file, use the SPM Display  
          option and move the crosshairs to a voxel coordinate of z=1.  This  
          corresponds to a point in the first slice of the volume.  
         
          The function corrects differences in slice acquisition times.  
          This routine is intended to correct for the staggered order of  
          slice acquisition that is used during echoplanar scanning. The  
          correction is necessary to make the data on each slice correspond  
          to the same point in time. Without correction, the data on one  
          slice will represent a point in time as far removed as 1/2 the TR  
          from an adjacent slice (in the case of an interleaved sequence).  
         
          This routine "shifts" a signal in time to provide an output  
          vector that represents the same (continuous) signal sampled  
          starting either later or earlier. This is accomplished by a simple  
          shift of the phase of the sines that make up the signal.  
         
          Recall that a Fourier transform allows for a representation of any  
          signal as the linear combination of sinusoids of different  
          frequencies and phases. Effectively, we will add a constant  
          to the phase of every frequency, shifting the data in time.  
         
          Shifter - This is the filter by which the signal will be convolved  
          to introduce the phase shift. It is constructed explicitly in  
          the Fourier domain. In the time domain, it may be described as  
          an impulse (delta function) that has been shifted in time the  
          amount described by TimeShift.  
         
          The correction works by lagging (shifting forward) the time-series  
          data on each slice using sinc-interpolation. This results in each  
          time series having the values that would have been obtained had  
          the slice been acquired at the same time as the reference slice.  
         
          To make this clear, consider a neural event (and ensuing hemodynamic  
          response) that occurs simultaneously on two adjacent slices. Values  
          from slice "A" are acquired starting at time zero, simultaneous to  
          the neural event, while values from slice "B" are acquired one  
          second later. Without correction, the "B" values will describe a  
          hemodynamic response that will appear to have began one second  
          EARLIER on the "B" slice than on slice "A". To correct for this,  
          the "B" values need to be shifted towards the Right, i.e., towards  
          the last value.  
         
        Written by Darren Gitelman at Northwestern U., 1998  
         
        Based (in large part) on ACQCORRECT.PRO from G. Aguirre and E. Zarahn  
        at U. Penn.  
         
        Modified by R. Henson, C. Buechel and J. Ashburner, FIL, to  
        handle different reference slices and memory mapping.  
         
        Modified by M. Erb, at U. Tuebingen, 1999, to ask for non-continuous  
        slice timing and number of sessions.  
         
        Modified by R. Henson for more general slice order and SPM2.  
         
        Modified by A. Hoffmann, M. Woletz and C. Windischberger from Medical  
        University of Vienna, Austria, to handle multi-band EPI sequences.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_slice_timing.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_slice_timing", *args, **kwargs, nargout=0)
