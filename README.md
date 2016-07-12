#Particle-Counter-Data-Analyzer
========
Particle count data analyzer; takes in a consolidated csv file and returns a detailed occupied vs unoccupied data analysis of a specific location at Sanford Undergraduate Research Facility (SURF)

Look how easy it is to use:

    1) *Update* 'MetOneAll.csv' at the end of the document by following the exixtisting structure (Row 1: date, Row 2:CF-.5 data and Row 3: Location with an optional Row 4: serial number of the particle counter). Please insert the following words for the location row:
    * Paticle counter located on the top the refrigrator of the davis campus: "Common Corridor Refrig" (without the quotes)
    * Particle counter inside MJD's clean room: "MJD Detector Room"
    * Particle counter inside MJD's machine room: "MJD Machine Room"
    * Particle counter located in BHSU's detector room:  "BHSU Brick Room"
    * Particle counter located at the IH surface office: "Surface IH Office"
    * Particle counter located at LL cavern north east corner: "LL Cavern NE Corner"
    * Particle counter located in E's count room: "E Count Room"
    * Particle counter located in E's counter room noth west corner: "E Count Room NW Corner
    * Particle counter located at the transition of from the entrace of the davis campus to the common corridor: "Transition W_D"
    2) *Compile and run* 'Analyzer_Mathplot.py' or 'Analyzer_Plotly.py' based on your data output choice and follow the prompts to the required data analysis output
    

Features
--------

* Take in row csv file and hourly and monthly plot the occupied and unoccupied data of the a specific locations
  * Analyzer_Mathplot.py: takes in the consolidated 'MetOneAll.csv' file and gives out either occupied or unoccupied hourly and monthly plot of the specified location at savable image using matplotlib library. It also gives out an HTML plot of the final analyzed data. 
  * Analyzer_Mathplot.py: takes in the consolidated 'MetOneAll.csv' file and gives out both the occupied and unccopied hourly and monthly plot of the specified location. 

Installation
------------

Download both 'Analyzer_Mathplot.py' and 'Analyzer_Mathplot.py' with 'MetOneAll.csv', compile and run the program of your choice!

Contribute
----------

- Issue Tracker: github.com/Josephss/Particle-Counter-Data-Analyzer/issues
- Source Code: github.com/Josephss/Particle-Counter-Data-Analyzer

Support
-------

If you are having issues, please let us know.
We have a mailing list located at: info@marvelouscode.com

License
-------

The project is licensed under the BSD license.
