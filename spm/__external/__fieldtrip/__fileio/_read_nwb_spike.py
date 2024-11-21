from spm.__wrapper__ import Runtime


def _read_nwb_spike(*args, **kwargs):
    """
      READ_NWB_SPIKE reads spike timestamps and waveforms (if present-not currently supported)   
        from NWB files and converts them to fieldtrip spike data format.   
         
        INPUT: filename = (Path and) name of the .nwb file  
         
        OUTPUT: spike = FieldTrip spike structure  
         
        Notes:   
        This function was written during the NWB hackathon May 2020. It is  
        based on example data in .nwb format schema version 2.0.1:   
        https://gui.dandiarchive.org/#/file-browser/folder/5e6eb2b776569eb93f451f8d  
         
        NWB is a complicated data format and under active development. We  
        recommend to use the latest stable release of MatNWB from the github  
        page: https://github.com/NeurodataWithoutBorders/matnwb/releases  
        and familiarize yourself with the use of generateCore():  
        https://neurodatawithoutborders.github.io/matnwb  
         
        With util.getSchemaVersion(file.nwb) the nwb file version can be  
        querried. It may be necessary to replace the files in ..\matnwb\nwb-schema\core  
        with the files from the nwb-schema version the file was created in from  
        ..\nwb-schema\core.   
        Nwb-schemas can be obtained from here:   
        https://github.com/NeurodataWithoutBorders/nwb-schema/releases  
          
        -----  
        Latest change: 01/06/2020  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_nwb_spike.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_nwb_spike", *args, **kwargs)
